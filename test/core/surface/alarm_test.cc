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

#include "src/core/lib/surface/completion_queue.h"

#include <grpc/alarm.h>
#include <grpc/support/alloc.h>
#include <grpc/support/log.h>
#include <grpc/support/time.h>
#include "src/core/lib/gpr/useful.h"
#include "src/core/lib/iomgr/iomgr.h"
#include "test/core/util/test_config.h"

#define LOG_TEST(x) gpr_log(GPR_INFO, "%s", x)

static void* create_test_tag(void) {
  static intptr_t i = 0;
  return (void*)(++i);
}

/* helper for tests to shutdown correctly and tersely */
static void shutdown_and_destroy(grpc_completion_queue* cc) {
  grpc_event ev;
  grpc_completion_queue_shutdown(cc);

  switch (grpc_get_cq_completion_type(cc)) {
    case GRPC_CQ_NEXT: {
      ev = grpc_completion_queue_next(cc, gpr_inf_past(GPR_CLOCK_REALTIME),
                                      nullptr);
      break;
    }
    case GRPC_CQ_PLUCK: {
      ev = grpc_completion_queue_pluck(
          cc, create_test_tag(), gpr_inf_past(GPR_CLOCK_REALTIME), nullptr);
      break;
    }
    default: {
      gpr_log(GPR_ERROR, "Unknown completion type");
      break;
    }
  }

  GPR_ASSERT(ev.type == GRPC_QUEUE_SHUTDOWN);
  grpc_completion_queue_destroy(cc);
}

static void test_alarm_notify(void) {
  grpc_alarm* alarm;
  grpc_event ev;
  grpc_completion_queue* cc;
  grpc_cq_polling_type polling_types[] = {
      GRPC_CQ_DEFAULT_POLLING, GRPC_CQ_NON_LISTENING, GRPC_CQ_NON_POLLING};
  grpc_completion_queue_attributes attr;
  void* tag = create_test_tag();

  LOG_TEST("test_alarm_notify");

  attr.version = 1;
  attr.cq_completion_type = GRPC_CQ_NEXT;
  for (size_t i = 0; i < GPR_ARRAY_SIZE(polling_types); i++) {
    attr.cq_polling_type = polling_types[i];
    cc = grpc_completion_queue_create(
        grpc_completion_queue_factory_lookup(&attr), &attr, nullptr);

    alarm = grpc_alarm_create(nullptr);
    grpc_alarm_set(alarm, cc, tag, nullptr);
    grpc_alarm_notify(alarm, nullptr);

   ev = grpc_completion_queue_next(cc, grpc_timeout_seconds_to_deadline(2),
                                    nullptr);
    GPR_ASSERT(ev.type == GRPC_OP_COMPLETE);
    GPR_ASSERT(ev.tag == tag);
    GPR_ASSERT(ev.success);

    grpc_alarm_destroy(alarm, nullptr);

    ev = grpc_completion_queue_next(cc, grpc_timeout_seconds_to_deadline(1),
                                    nullptr);
    GPR_ASSERT(ev.type == GRPC_QUEUE_TIMEOUT);
    GPR_ASSERT(ev.tag == nullptr);
    GPR_ASSERT(!ev.success);

    shutdown_and_destroy(cc);
  }
}

static void test_alarm_destroy(void) {
  grpc_alarm* alarm;
  grpc_event ev;
  grpc_completion_queue* cc;
  grpc_cq_polling_type polling_types[] = {
      GRPC_CQ_DEFAULT_POLLING, GRPC_CQ_NON_LISTENING, GRPC_CQ_NON_POLLING};
  grpc_completion_queue_attributes attr;
  void* tag = create_test_tag();

  LOG_TEST("test_alarm_destroy");

  attr.version = 1;
  attr.cq_completion_type = GRPC_CQ_NEXT;
  for (size_t i = 0; i < GPR_ARRAY_SIZE(polling_types); i++) {
    attr.cq_polling_type = polling_types[i];
    cc = grpc_completion_queue_create(
        grpc_completion_queue_factory_lookup(&attr), &attr, nullptr);

    alarm = grpc_alarm_create(nullptr);
    grpc_alarm_set(alarm, cc, tag, nullptr);
    grpc_alarm_destroy(alarm, nullptr);

    ev = grpc_completion_queue_next(cc, grpc_timeout_seconds_to_deadline(2),
                                    nullptr);
    GPR_ASSERT(ev.type == GRPC_OP_COMPLETE);
    GPR_ASSERT(ev.tag == tag);
    GPR_ASSERT(!ev.success);

    shutdown_and_destroy(cc);
  }
}
int main(int argc, char** argv) {
  grpc_test_init(argc, argv);
  grpc_init();
  test_alarm_notify();
  test_alarm_destroy();
  grpc_shutdown();
  return 0;
}
