// Copyright 2023 TiKV Project Authors. Licensed under Apache-2.0.

#include <include/grpcrs/stats.h>

#include "src/core/lib/debug/stats.h"
#include "src/core/lib/debug/stats_data.h"

// Just make sure they have the same number of counters.
static_assert(static_cast<int>(grpcrs_stats_counter::COUNTER_COUNT) ==
                  static_cast<int>(grpc_core::GlobalStats::Counter::COUNT),
              "Counter count must be the same");

// Just make sure they have the same number of histograms.
static_assert(static_cast<int>(grpcrs_stats_histogram::HISTOGRAM_COUNT) ==
                  static_cast<int>(grpc_core::GlobalStats::Histogram::COUNT),
              "Histogram count must be the same");

grpcrs_stats* grpcrs_stats_collect() {
  return (grpcrs_stats*)grpc_core::global_stats().Collect().release();
}

void grpcrs_stats_free(grpcrs_stats* stats) {
  auto s = (grpc_core::GlobalStats*)stats;
  delete s;
}

uint64_t grpcrs_stats_get_counter(
    const grpcrs_stats* stats, grpcrs_stats_counter which) {
  auto s = (const grpc_core::GlobalStats*)stats;
  return s->counters[which];
}

grpc_slice
grpcrs_stats_counter_name(grpcrs_stats_counter which) {
  auto name = grpc_core::GlobalStats::counter_name[which];
  auto slice = grpc_slice_from_static_buffer(name.data(), name.size());
  return slice;
}

grpc_slice
grpcrs_stats_counter_doc(grpcrs_stats_counter which) {
  auto doc = grpc_core::GlobalStats::counter_doc[which];
  auto slice = grpc_slice_from_static_buffer(doc.data(), doc.size());
  return slice;
}

double grpcrs_stats_get_histogram_percentile(
    const grpcrs_stats* stats, grpcrs_stats_histogram which,
    double percentile) {
  auto s = (const grpc_core::GlobalStats*)stats;
  return s->histogram(static_cast<grpc_core::GlobalStats::Histogram>(which))
      .Percentile(percentile);
}

double grpcrs_stats_get_histogram_count(
    const grpcrs_stats* stats, grpcrs_stats_histogram which) {
  auto s = (const grpc_core::GlobalStats*)stats;
  return s->histogram(static_cast<grpc_core::GlobalStats::Histogram>(which))
      .Count();
}

grpc_slice
grpcrs_stats_histogram_name(grpcrs_stats_histogram which) {
  auto name = grpc_core::GlobalStats::histogram_name[which];
  auto slice = grpc_slice_from_static_buffer(name.data(), name.size());
  return slice;
}

grpc_slice
grpcrs_stats_histogram_doc(grpcrs_stats_histogram which) {
  auto doc = grpc_core::GlobalStats::histogram_doc[which];
  auto slice = grpc_slice_from_static_buffer(doc.data(), doc.size());
  return slice;
}
