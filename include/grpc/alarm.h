/*
 *
 * Copyright 2015-2016 gRPC authors.
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

#ifndef GRPC_ALARM_H
#define GRPC_ALARM_H

#include <grpc/impl/codegen/grpc_types.h>

#ifdef __cplusplus
extern "C" {
#endif

/** Create a completion queue alarm instance */
GRPCAPI grpc_alarm* grpc_alarm_create(void* reserved);

/** Set a completion queue alarm instance associated to \a cq.
 *
 * Once the alarm notifies (see \a grpc_alarm_notify) or it's destroy (see \a
 * grpc_alarm_destroy), an event with tag \a tag will be added to \a cq. If the
 * alarm notified, the event's success bit will be true, false otherwise. */
GRPCAPI void grpc_alarm_set(grpc_alarm* alarm, grpc_completion_queue* cq,
                            void* tag, void* reserved);

/** Notify a completion queue alarm. Calling this function over an alarm that
 * has already fired has no effect. */
GRPCAPI void grpc_alarm_notify(grpc_alarm* alarm, void* reserved);

/** Destroy the given completion queue alarm, cancelling it in the process. */
GRPCAPI void grpc_alarm_destroy(grpc_alarm* alarm, void* reserved);

#ifdef __cplusplus
}
#endif

#endif /* GRPC_ALARM_H */
