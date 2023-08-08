// Copyright 2023 TiKV Project Authors. Licensed under Apache-2.0.

#ifndef GRPC_RS_STATS_H
#define GRPC_RS_STATS_H

#include <grpc/support/port_platform.h>
#include <grpc/slice.h>

#ifndef GRPCRSAPI
#define GRPCRSAPI GPRAPI
#endif

#ifdef __cplusplus
extern "C" {
#endif

/** gRPC stats.
    See: grpc/src/core/lib/debug/stats_data.yaml */
typedef struct grpcrs_stats grpcrs_stats;

enum grpcrs_stats_counter {
  ClientCallsCreated,
  ServerCallsCreated,
  ClientChannelsCreated,
  ClientSubchannelsCreated,
  ServerChannelsCreated,
  InsecureConnectionsCreated,
  SyscallWrite,
  SyscallRead,
  TcpReadAlloc8k,
  TcpReadAlloc64k,
  Http2SettingsWrites,
  Http2PingsSent,
  Http2WritesBegun,
  Http2TransportStalls,
  Http2StreamStalls,
  CqPluckCreates,
  CqNextCreates,
  CqCallbackCreates,
  COUNTER_COUNT
};

enum grpcrs_stats_histogram {
  CallInitialSize,
  TcpWriteSize,
  TcpWriteIovSize,
  TcpReadSize,
  TcpReadOffer,
  TcpReadOfferIovSize,
  Http2SendMessageSize,
  Http2MetadataSize,
  HISTOGRAM_COUNT
};

GRPCRSAPI grpcrs_stats* grpcrs_stats_collect();

GRPCRSAPI void grpcrs_stats_free(grpcrs_stats* stats);

GRPCRSAPI uint64_t grpcrs_stats_get_counter(
    const grpcrs_stats* stats, grpcrs_stats_counter which);

GRPCRSAPI grpc_slice grpcrs_stats_counter_name(grpcrs_stats_counter which);

GRPCRSAPI grpc_slice grpcrs_stats_counter_doc(grpcrs_stats_counter which);

GRPCRSAPI double grpcrs_stats_get_histogram_percentile(
    const grpcrs_stats* stats, grpcrs_stats_histogram which,
    double percentile);

GRPCRSAPI double grpcrs_stats_get_histogram_count(
    const grpcrs_stats* stats, grpcrs_stats_histogram which);

GRPCRSAPI grpc_slice grpcrs_stats_histogram_name(grpcrs_stats_histogram which);

GRPCRSAPI grpc_slice grpcrs_stats_histogram_doc(grpcrs_stats_histogram which);

#ifdef __cplusplus
}
#endif

#endif /* GRPC_RS_STATS_H */
