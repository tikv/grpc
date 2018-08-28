/*
 *
 * Copyright 2018 PingCAP authors.
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

/*
 *
 * Copyright 2016 gRPC authors.
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

#include <grpcpp/alarm.h>
#include <sstream>

#include "src/proto/grpc/testing/echo.grpc.pb.h"
#include "test/cpp/microbenchmarks/fullstack_fixtures.h"

namespace grpc {
namespace testing {

/*******************************************************************************
 * BENCHMARKING KERNELS
 */

class InsecureCallKicker : public FullstackFixture {
 public:
  InsecureCallKicker(Service* service, void* tag)
      : FullstackFixture(service, FixtureConfiguration(), MakeAddress(&port_)),
        tag_(tag) {
    grpc_completion_queue* cq = InsecureCallKicker::cq();
    grpc::string host = InsecureCallKicker::Host(port_);
    grpc_slice method = grpc_empty_slice();
    ChannelArguments args;
    FixtureConfiguration().ApplyCommonChannelArguments(&args);
    grpc_channel_args channel_args;
    args.SetChannelArgs(&channel_args);
    channel_ =
        grpc_insecure_channel_create(host.c_str(), &channel_args, nullptr);
    grpc_slice call_host = grpc_slice_from_copied_string(host.c_str());
    call_ =
        grpc_channel_create_call(channel_, nullptr, 0, cq, method, &call_host,
                                 gpr_inf_future(GPR_CLOCK_MONOTONIC), nullptr);
  }

  ~InsecureCallKicker() {
    grpc_call_unref(call_);
    grpc_channel_destroy(channel_);
    grpc_recycle_unused_port(port_);
  }

  grpc_completion_queue* cq() { return FullstackFixture::cq()->cq(); }

  void kick() {
    grpc_call_start_batch(call_, nullptr, 0, tag_, nullptr);
    return;
  }

  void post_kick() { return; }

 private:
  int port_;
  grpc_channel* channel_;
  grpc_call* call_;
  void* tag_;

  static grpc::string Host(int port) {
    std::stringstream addr;
    addr << "localhost:" << port;
    return addr.str();
  }

  static grpc::string MakeAddress(int* port) {
    *port = grpc_pick_unused_port_or_die();
    return Host(*port);
  }
};

class AlarmKicker : public TrackCounters {
 public:
  AlarmKicker(Service* _, void* tag) : cq_(CompletionQueue()), tag_(tag) {}

  grpc_completion_queue* cq() { return cq_.cq(); }

  void kick() {
    alarm_ = new Alarm;
    alarm_->Set(&cq_, gpr_inf_future(GPR_CLOCK_MONOTONIC), tag_);
    alarm_->Cancel();
    return;
  }

  void post_kick() {
    delete alarm_;
    return;
  }

 private:
  Alarm* alarm_;
  CompletionQueue cq_;
  void* tag_;
};

template <class Fixture>
static void BM_KickCq(benchmark::State& state) {
  EchoTestService::AsyncService service;
  void* junk = reinterpret_cast<void*>(1618033);
  std::unique_ptr<Fixture> fixture(new Fixture(&service, junk));
  grpc_completion_queue* cq = fixture->cq();

  while (state.KeepRunning()) {
    fixture->kick();
    grpc_completion_queue_next(cq, gpr_inf_future(GPR_CLOCK_MONOTONIC),
                               nullptr);
    fixture->post_kick();
  }
  fixture->Finish(state);
}

}  // namespace testing
}  // namespace grpc
