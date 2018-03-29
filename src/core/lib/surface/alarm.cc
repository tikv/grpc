/*
 *
 * Copyright 2015 gRPC authors.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 *
 */
#include <grpc/support/port_platform.h>

#include <inttypes.h>

#include <grpc/alarm.h>
#include <grpc/grpc.h>
#include <grpc/support/alloc.h>
#include <grpc/support/log.h>
#include "src/core/lib/debug/trace.h"
#include "src/core/lib/surface/completion_queue.h"

#ifndef NDEBUG

#define GRPC_ALARM_REF(a, reason) alarm_ref_dbg(a, reason, __FILE__, __LINE__)
#define GRPC_ALARM_UNREF(a, reason) \
  alarm_unref_dbg(a, reason, __FILE__, __LINE__)

#else /* !defined(NDEBUG) */

#define GRPC_ALARM_REF(a, reason) alarm_ref(a)
#define GRPC_ALARM_UNREF(a, reason) alarm_unref(a)

#endif /* defined(NDEBUG) */

grpc_core::DebugOnlyTraceFlag grpc_trace_alarm_refcount(false,
                                                        "alarm_refcount");

struct grpc_alarm {
  gpr_refcount refs;
  gpr_atm alarmed;
  grpc_closure on_alarm;
  grpc_cq_completion completion;
  /** completion queue where events about this alarm will be posted */
  grpc_completion_queue* cq;
  /** user supplied tag */
  void* tag;
};

static void alarm_ref(grpc_alarm* alarm) { gpr_ref(&alarm->refs); }

static void alarm_unref(grpc_alarm* alarm) {
  if (gpr_unref(&alarm->refs)) {
    grpc_core::ExecCtx exec_ctx;
    if (alarm->cq != nullptr) {
      GRPC_CQ_INTERNAL_UNREF(alarm->cq, "alarm");
    }

    gpr_free(alarm);
  }
}

#ifndef NDEBUG
static void alarm_ref_dbg(grpc_alarm* alarm, const char* reason,
                          const char* file, int line) {
  if (grpc_trace_alarm_refcount.enabled()) {
    gpr_atm val = gpr_atm_no_barrier_load(&alarm->refs.count);
    gpr_log(file, line, GPR_LOG_SEVERITY_DEBUG,
            "Alarm:%p  ref %" PRIdPTR " -> %" PRIdPTR " %s", alarm, val,
            val + 1, reason);
  }

  alarm_ref(alarm);
}

static void alarm_unref_dbg(grpc_alarm* alarm, const char* reason,
                            const char* file, int line) {
  if (grpc_trace_alarm_refcount.enabled()) {
    gpr_atm val = gpr_atm_no_barrier_load(&alarm->refs.count);
    gpr_log(file, line, GPR_LOG_SEVERITY_DEBUG,
            "Alarm:%p  Unref %" PRIdPTR " -> %" PRIdPTR " %s", alarm, val,
            val - 1, reason);
  }

  alarm_unref(alarm);
}
#endif

static void alarm_end_completion(void* arg, grpc_cq_completion* c) {
  grpc_alarm* alarm = (grpc_alarm*)arg;
  GRPC_ALARM_UNREF(alarm, "dequeue-end-op");
}

static void alarm_cb(void* arg, grpc_error* error) {
  grpc_alarm* alarm = (grpc_alarm*)arg;

  /* We are queuing an op on completion queue. This means, the alarm's structure
     cannot be destroyed until the op is dequeued. Adding an extra ref
     here and unref'ing when the op is dequeued will achieve this */
  GRPC_ALARM_REF(alarm, "queue-end-op");
  grpc_cq_end_op(alarm->cq, alarm->tag, error, alarm_end_completion,
                 (void*)alarm, &alarm->completion);
}

static void grpc_alarm_raise(grpc_alarm* alarm, grpc_error* error) {
  grpc_core::ExecCtx exec_ctx;
  size_t alarmed = static_cast<size_t>(
      gpr_atm_full_fetch_add(&alarm->alarmed, (gpr_atm)1));
  if (!alarmed) {
    GRPC_CLOSURE_SCHED(&alarm->on_alarm, error);
  }
}

grpc_alarm* grpc_alarm_create(void* reserved) {
  grpc_alarm* alarm = (grpc_alarm*)gpr_malloc(sizeof(grpc_alarm));

#ifndef NDEBUG
  if (grpc_trace_alarm_refcount.enabled()) {
    gpr_log(GPR_DEBUG, "Alarm:%p created (ref: 1)", alarm);
  }
#endif

  gpr_ref_init(&alarm->refs, 1);
  alarm->cq = nullptr;
  alarm->alarmed = (gpr_atm)0;
  GRPC_CLOSURE_INIT(&alarm->on_alarm, alarm_cb, alarm,
                    grpc_schedule_on_exec_ctx);
  return alarm;
}

void grpc_alarm_set(grpc_alarm* alarm, grpc_completion_queue* cq,
                    void* tag, void* reserved) {
  grpc_core::ExecCtx exec_ctx;

  GRPC_CQ_INTERNAL_REF(cq, "alarm");
  alarm->cq = cq;
  alarm->tag = tag;

  GPR_ASSERT(grpc_cq_begin_op(cq, tag));
}

void grpc_alarm_notify(grpc_alarm* alarm, void* reserved) {
  grpc_alarm_raise(alarm, GRPC_ERROR_NONE);
}

void grpc_alarm_destroy(grpc_alarm* alarm, void* reserved) {
  grpc_alarm_raise(alarm, GRPC_ERROR_CANCELLED);
  GRPC_ALARM_UNREF(alarm, "alarm_destroy");
}
