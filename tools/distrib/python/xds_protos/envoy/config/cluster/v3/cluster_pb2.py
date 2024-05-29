# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/config/cluster/v3/cluster.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.cluster.v3 import circuit_breaker_pb2 as envoy_dot_config_dot_cluster_dot_v3_dot_circuit__breaker__pb2
from envoy.config.cluster.v3 import filter_pb2 as envoy_dot_config_dot_cluster_dot_v3_dot_filter__pb2
from envoy.config.cluster.v3 import outlier_detection_pb2 as envoy_dot_config_dot_cluster_dot_v3_dot_outlier__detection__pb2
from envoy.config.core.v3 import address_pb2 as envoy_dot_config_dot_core_dot_v3_dot_address__pb2
from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from envoy.config.core.v3 import config_source_pb2 as envoy_dot_config_dot_core_dot_v3_dot_config__source__pb2
from envoy.config.core.v3 import extension_pb2 as envoy_dot_config_dot_core_dot_v3_dot_extension__pb2
from envoy.config.core.v3 import health_check_pb2 as envoy_dot_config_dot_core_dot_v3_dot_health__check__pb2
from envoy.config.core.v3 import protocol_pb2 as envoy_dot_config_dot_core_dot_v3_dot_protocol__pb2
from envoy.config.core.v3 import resolver_pb2 as envoy_dot_config_dot_core_dot_v3_dot_resolver__pb2
from envoy.config.endpoint.v3 import endpoint_pb2 as envoy_dot_config_dot_endpoint_dot_v3_dot_endpoint__pb2
from envoy.type.metadata.v3 import metadata_pb2 as envoy_dot_type_dot_metadata_dot_v3_dot_metadata__pb2
from envoy.type.v3 import percent_pb2 as envoy_dot_type_dot_v3_dot_percent__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import duration_pb2 as google_dot_protobuf_dot_duration__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from xds.core.v3 import collection_entry_pb2 as xds_dot_core_dot_v3_dot_collection__entry__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import migrate_pb2 as udpa_dot_annotations_dot_migrate__pb2
from udpa.annotations import security_pb2 as udpa_dot_annotations_dot_security__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%envoy/config/cluster/v3/cluster.proto\x12\x17\x65nvoy.config.cluster.v3\x1a-envoy/config/cluster/v3/circuit_breaker.proto\x1a$envoy/config/cluster/v3/filter.proto\x1a/envoy/config/cluster/v3/outlier_detection.proto\x1a\"envoy/config/core/v3/address.proto\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a(envoy/config/core/v3/config_source.proto\x1a$envoy/config/core/v3/extension.proto\x1a\'envoy/config/core/v3/health_check.proto\x1a#envoy/config/core/v3/protocol.proto\x1a#envoy/config/core/v3/resolver.proto\x1a\'envoy/config/endpoint/v3/endpoint.proto\x1a%envoy/type/metadata/v3/metadata.proto\x1a\x1b\x65nvoy/type/v3/percent.proto\x1a\x19google/protobuf/any.proto\x1a\x1egoogle/protobuf/duration.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a\x1egoogle/protobuf/wrappers.proto\x1a\"xds/core/v3/collection_entry.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1eudpa/annotations/migrate.proto\x1a\x1fudpa/annotations/security.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\x1a\x17validate/validate.proto\"B\n\x11\x43lusterCollection\x12-\n\x07\x65ntries\x18\x01 \x01(\x0b\x32\x1c.xds.core.v3.CollectionEntry\"\xb9\x44\n\x07\x43luster\x12W\n\x18transport_socket_matches\x18+ \x03(\x0b\x32\x35.envoy.config.cluster.v3.Cluster.TransportSocketMatch\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x31\n\ralt_stat_name\x18\x1c \x01(\tB\x1a\xf2\x98\xfe\x8f\x05\x14\n\x12observability_name\x12H\n\x04type\x18\x02 \x01(\x0e\x32..envoy.config.cluster.v3.Cluster.DiscoveryTypeB\x08\xfa\x42\x05\x82\x01\x02\x10\x01H\x00\x12J\n\x0c\x63luster_type\x18& \x01(\x0b\x32\x32.envoy.config.cluster.v3.Cluster.CustomClusterTypeH\x00\x12M\n\x12\x65\x64s_cluster_config\x18\x03 \x01(\x0b\x32\x31.envoy.config.cluster.v3.Cluster.EdsClusterConfig\x12<\n\x0f\x63onnect_timeout\x18\x04 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02*\x00\x12P\n!per_connection_buffer_limit_bytes\x18\x05 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\x8a\x93\xb7*\x02\x10\x01\x12\x46\n\tlb_policy\x18\x06 \x01(\x0e\x32).envoy.config.cluster.v3.Cluster.LbPolicyB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12H\n\x0fload_assignment\x18! \x01(\x0b\x32/.envoy.config.endpoint.v3.ClusterLoadAssignment\x12\x38\n\rhealth_checks\x18\x08 \x03(\x0b\x32!.envoy.config.core.v3.HealthCheck\x12N\n\x1bmax_requests_per_connection\x18\t \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12\x42\n\x10\x63ircuit_breakers\x18\n \x01(\x0b\x32(.envoy.config.cluster.v3.CircuitBreakers\x12\x66\n\x1eupstream_http_protocol_options\x18. \x01(\x0b\x32\x31.envoy.config.core.v3.UpstreamHttpProtocolOptionsB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12\\\n\x1c\x63ommon_http_protocol_options\x18\x1d \x01(\x0b\x32).envoy.config.core.v3.HttpProtocolOptionsB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12V\n\x15http_protocol_options\x18\r \x01(\x0b\x32*.envoy.config.core.v3.Http1ProtocolOptionsB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12^\n\x16http2_protocol_options\x18\x0e \x01(\x0b\x32*.envoy.config.core.v3.Http2ProtocolOptionsB\x12\x18\x01\x8a\x93\xb7*\x02\x10\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12m\n typed_extension_protocol_options\x18$ \x03(\x0b\x32\x43.envoy.config.cluster.v3.Cluster.TypedExtensionProtocolOptionsEntry\x12\x41\n\x10\x64ns_refresh_rate\x18\x10 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06*\x04\x10\xc0\x84=\x12N\n\x18\x64ns_failure_refresh_rate\x18, \x01(\x0b\x32,.envoy.config.cluster.v3.Cluster.RefreshRate\x12\x17\n\x0frespect_dns_ttl\x18\' \x01(\x08\x12U\n\x11\x64ns_lookup_family\x18\x11 \x01(\x0e\x32\x30.envoy.config.cluster.v3.Cluster.DnsLookupFamilyB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x41\n\rdns_resolvers\x18\x12 \x03(\x0b\x32\x1d.envoy.config.core.v3.AddressB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12,\n\x17use_tcp_for_dns_lookups\x18- \x01(\x08\x42\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12U\n\x15\x64ns_resolution_config\x18\x35 \x01(\x0b\x32).envoy.config.core.v3.DnsResolutionConfigB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12M\n\x19typed_dns_resolver_config\x18\x37 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfig\x12\x39\n\x15wait_for_warm_on_init\x18\x36 \x01(\x0b\x32\x1a.google.protobuf.BoolValue\x12\x44\n\x11outlier_detection\x18\x13 \x01(\x0b\x32).envoy.config.cluster.v3.OutlierDetection\x12=\n\x10\x63leanup_interval\x18\x14 \x01(\x0b\x32\x19.google.protobuf.DurationB\x08\xfa\x42\x05\xaa\x01\x02*\x00\x12>\n\x14upstream_bind_config\x18\x15 \x01(\x0b\x32 .envoy.config.core.v3.BindConfig\x12I\n\x10lb_subset_config\x18\x16 \x01(\x0b\x32/.envoy.config.cluster.v3.Cluster.LbSubsetConfig\x12P\n\x13ring_hash_lb_config\x18\x17 \x01(\x0b\x32\x31.envoy.config.cluster.v3.Cluster.RingHashLbConfigH\x01\x12K\n\x10maglev_lb_config\x18\x34 \x01(\x0b\x32/.envoy.config.cluster.v3.Cluster.MaglevLbConfigH\x01\x12V\n\x16original_dst_lb_config\x18\" \x01(\x0b\x32\x34.envoy.config.cluster.v3.Cluster.OriginalDstLbConfigH\x01\x12X\n\x17least_request_lb_config\x18% \x01(\x0b\x32\x35.envoy.config.cluster.v3.Cluster.LeastRequestLbConfigH\x01\x12T\n\x15round_robin_lb_config\x18\x38 \x01(\x0b\x32\x33.envoy.config.cluster.v3.Cluster.RoundRobinLbConfigH\x01\x12I\n\x10\x63ommon_lb_config\x18\x1b \x01(\x0b\x32/.envoy.config.cluster.v3.Cluster.CommonLbConfig\x12?\n\x10transport_socket\x18\x18 \x01(\x0b\x32%.envoy.config.core.v3.TransportSocket\x12\x30\n\x08metadata\x18\x19 \x01(\x0b\x32\x1e.envoy.config.core.v3.Metadata\x12\x62\n\x12protocol_selection\x18\x1a \x01(\x0e\x32\x39.envoy.config.cluster.v3.Cluster.ClusterProtocolSelectionB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12W\n\x1bupstream_connection_options\x18\x1e \x01(\x0b\x32\x32.envoy.config.cluster.v3.UpstreamConnectionOptions\x12\x30\n(close_connections_on_host_health_failure\x18\x1f \x01(\x08\x12%\n\x1dignore_health_on_host_removal\x18  \x01(\x08\x12\x30\n\x07\x66ilters\x18( \x03(\x0b\x32\x1f.envoy.config.cluster.v3.Filter\x12K\n\x15load_balancing_policy\x18) \x01(\x0b\x32,.envoy.config.cluster.v3.LoadBalancingPolicy\x12\x36\n\nlrs_server\x18* \x01(\x0b\x32\".envoy.config.core.v3.ConfigSource\x12*\n\x15track_timeout_budgets\x18/ \x01(\x08\x42\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12\x43\n\x0fupstream_config\x18\x30 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfig\x12G\n\x13track_cluster_stats\x18\x31 \x01(\x0b\x32*.envoy.config.cluster.v3.TrackClusterStats\x12L\n\x11preconnect_policy\x18\x32 \x01(\x0b\x32\x31.envoy.config.cluster.v3.Cluster.PreconnectPolicy\x12\x31\n)connection_pool_per_downstream_connection\x18\x33 \x01(\x08\x1a\xc8\x01\n\x14TransportSocketMatch\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12&\n\x05match\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12?\n\x10transport_socket\x18\x03 \x01(\x0b\x32%.envoy.config.core.v3.TransportSocket:0\x9a\xc5\x88\x1e+\n)envoy.api.v2.Cluster.TransportSocketMatch\x1a\x85\x01\n\x11\x43ustomClusterType\x12\x15\n\x04name\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12*\n\x0ctyped_config\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:-\x9a\xc5\x88\x1e(\n&envoy.api.v2.Cluster.CustomClusterType\x1a\x8e\x01\n\x10\x45\x64sClusterConfig\x12\x36\n\neds_config\x18\x01 \x01(\x0b\x32\".envoy.config.core.v3.ConfigSource\x12\x14\n\x0cservice_name\x18\x02 \x01(\t:,\x9a\xc5\x88\x1e\'\n%envoy.api.v2.Cluster.EdsClusterConfig\x1a\xd9\x08\n\x0eLbSubsetConfig\x12i\n\x0f\x66\x61llback_policy\x18\x01 \x01(\x0e\x32\x46.envoy.config.cluster.v3.Cluster.LbSubsetConfig.LbSubsetFallbackPolicyB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12/\n\x0e\x64\x65\x66\x61ult_subset\x18\x02 \x01(\x0b\x32\x17.google.protobuf.Struct\x12Z\n\x10subset_selectors\x18\x03 \x03(\x0b\x32@.envoy.config.cluster.v3.Cluster.LbSubsetConfig.LbSubsetSelector\x12\x1d\n\x15locality_weight_aware\x18\x04 \x01(\x08\x12\x1d\n\x15scale_locality_weight\x18\x05 \x01(\x08\x12\x16\n\x0epanic_mode_any\x18\x06 \x01(\x08\x12\x13\n\x0blist_as_any\x18\x07 \x01(\x08\x12z\n\x18metadata_fallback_policy\x18\x08 \x01(\x0e\x32N.envoy.config.cluster.v3.Cluster.LbSubsetConfig.LbSubsetMetadataFallbackPolicyB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x1a\x9b\x03\n\x10LbSubsetSelector\x12\x0c\n\x04keys\x18\x01 \x03(\t\x12\x1e\n\x16single_host_per_subset\x18\x04 \x01(\x08\x12\x82\x01\n\x0f\x66\x61llback_policy\x18\x02 \x01(\x0e\x32_.envoy.config.cluster.v3.Cluster.LbSubsetConfig.LbSubsetSelector.LbSubsetSelectorFallbackPolicyB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x1c\n\x14\x66\x61llback_keys_subset\x18\x03 \x03(\t\"y\n\x1eLbSubsetSelectorFallbackPolicy\x12\x0f\n\x0bNOT_DEFINED\x10\x00\x12\x0f\n\x0bNO_FALLBACK\x10\x01\x12\x10\n\x0c\x41NY_ENDPOINT\x10\x02\x12\x12\n\x0e\x44\x45\x46\x41ULT_SUBSET\x10\x03\x12\x0f\n\x0bKEYS_SUBSET\x10\x04:;\x9a\xc5\x88\x1e\x36\n4envoy.api.v2.Cluster.LbSubsetConfig.LbSubsetSelector\"O\n\x16LbSubsetFallbackPolicy\x12\x0f\n\x0bNO_FALLBACK\x10\x00\x12\x10\n\x0c\x41NY_ENDPOINT\x10\x01\x12\x12\n\x0e\x44\x45\x46\x41ULT_SUBSET\x10\x02\"M\n\x1eLbSubsetMetadataFallbackPolicy\x12\x18\n\x14METADATA_NO_FALLBACK\x10\x00\x12\x11\n\rFALLBACK_LIST\x10\x01:*\x9a\xc5\x88\x1e%\n#envoy.api.v2.Cluster.LbSubsetConfig\x1a\xb4\x01\n\x0fSlowStartConfig\x12\x34\n\x11slow_start_window\x18\x01 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\x37\n\naggression\x18\x02 \x01(\x0b\x32#.envoy.config.core.v3.RuntimeDouble\x12\x32\n\x12min_weight_percent\x18\x03 \x01(\x0b\x32\x16.envoy.type.v3.Percent\x1a\x61\n\x12RoundRobinLbConfig\x12K\n\x11slow_start_config\x18\x01 \x01(\x0b\x32\x30.envoy.config.cluster.v3.Cluster.SlowStartConfig\x1a\x94\x02\n\x14LeastRequestLbConfig\x12;\n\x0c\x63hoice_count\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02(\x02\x12@\n\x13\x61\x63tive_request_bias\x18\x02 \x01(\x0b\x32#.envoy.config.core.v3.RuntimeDouble\x12K\n\x11slow_start_config\x18\x03 \x01(\x0b\x32\x30.envoy.config.cluster.v3.Cluster.SlowStartConfig:0\x9a\xc5\x88\x1e+\n)envoy.api.v2.Cluster.LeastRequestLbConfig\x1a\xe1\x02\n\x10RingHashLbConfig\x12\x43\n\x11minimum_ring_size\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\n\xfa\x42\x07\x32\x05\x18\x80\x80\x80\x04\x12_\n\rhash_function\x18\x03 \x01(\x0e\x32>.envoy.config.cluster.v3.Cluster.RingHashLbConfig.HashFunctionB\x08\xfa\x42\x05\x82\x01\x02\x10\x01\x12\x43\n\x11maximum_ring_size\x18\x04 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\n\xfa\x42\x07\x32\x05\x18\x80\x80\x80\x04\".\n\x0cHashFunction\x12\x0b\n\x07XX_HASH\x10\x00\x12\x11\n\rMURMUR_HASH_2\x10\x01:,\x9a\xc5\x88\x1e\'\n%envoy.api.v2.Cluster.RingHashLbConfigJ\x04\x08\x02\x10\x03\x1aN\n\x0eMaglevLbConfig\x12<\n\ntable_size\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.UInt64ValueB\n\xfa\x42\x07\x32\x05\x18\xcb\x96\xb1\x02\x1a\xfd\x01\n\x13OriginalDstLbConfig\x12\x17\n\x0fuse_http_header\x18\x01 \x01(\x08\x12\x18\n\x10http_header_name\x18\x02 \x01(\t\x12G\n\x16upstream_port_override\x18\x03 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\t\xfa\x42\x06*\x04\x18\xff\xff\x03\x12\x39\n\x0cmetadata_key\x18\x04 \x01(\x0b\x32#.envoy.type.metadata.v3.MetadataKey:/\x9a\xc5\x88\x1e*\n(envoy.api.v2.Cluster.OriginalDstLbConfig\x1a\xb2\t\n\x0e\x43ommonLbConfig\x12\x37\n\x17healthy_panic_threshold\x18\x01 \x01(\x0b\x32\x16.envoy.type.v3.Percent\x12\x61\n\x14zone_aware_lb_config\x18\x02 \x01(\x0b\x32\x41.envoy.config.cluster.v3.Cluster.CommonLbConfig.ZoneAwareLbConfigH\x00\x12o\n\x1blocality_weighted_lb_config\x18\x03 \x01(\x0b\x32H.envoy.config.cluster.v3.Cluster.CommonLbConfig.LocalityWeightedLbConfigH\x00\x12\x36\n\x13update_merge_window\x18\x04 \x01(\x0b\x32\x19.google.protobuf.Duration\x12\'\n\x1fignore_new_hosts_until_first_hc\x18\x05 \x01(\x08\x12,\n$close_connections_on_host_set_change\x18\x06 \x01(\x08\x12o\n\x1c\x63onsistent_hashing_lb_config\x18\x07 \x01(\x0b\x32I.envoy.config.cluster.v3.Cluster.CommonLbConfig.ConsistentHashingLbConfig\x12\x43\n\x14override_host_status\x18\x08 \x01(\x0b\x32%.envoy.config.core.v3.HealthStatusSet\x1a\xd9\x01\n\x11ZoneAwareLbConfig\x12/\n\x0frouting_enabled\x18\x01 \x01(\x0b\x32\x16.envoy.type.v3.Percent\x12\x36\n\x10min_cluster_size\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt64Value\x12\x1d\n\x15\x66\x61il_traffic_on_panic\x18\x03 \x01(\x08:<\x9a\xc5\x88\x1e\x37\n5envoy.api.v2.Cluster.CommonLbConfig.ZoneAwareLbConfig\x1a_\n\x18LocalityWeightedLbConfig:C\x9a\xc5\x88\x1e>\n<envoy.api.v2.Cluster.CommonLbConfig.LocalityWeightedLbConfig\x1a\xc7\x01\n\x19\x43onsistentHashingLbConfig\x12 \n\x18use_hostname_for_hashing\x18\x01 \x01(\x08\x12\x42\n\x13hash_balance_factor\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.UInt32ValueB\x07\xfa\x42\x04*\x02(d:D\x9a\xc5\x88\x1e?\n=envoy.api.v2.Cluster.CommonLbConfig.ConsistentHashingLbConfig:*\x9a\xc5\x88\x1e%\n#envoy.api.v2.Cluster.CommonLbConfigB\x1b\n\x19locality_config_specifier\x1a\xb7\x01\n\x0bRefreshRate\x12@\n\rbase_interval\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0e\xfa\x42\x0b\xaa\x01\x08\x08\x01*\x04\x10\xc0\x84=\x12=\n\x0cmax_interval\x18\x02 \x01(\x0b\x32\x19.google.protobuf.DurationB\x0c\xfa\x42\t\xaa\x01\x06*\x04\x10\xc0\x84=:\'\x9a\xc5\x88\x1e\"\n envoy.api.v2.Cluster.RefreshRate\x1a\xcc\x01\n\x10PreconnectPolicy\x12\\\n\x1dper_upstream_preconnect_ratio\x18\x01 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\x08@)\x00\x00\x00\x00\x00\x00\xf0?\x12Z\n\x1bpredictive_preconnect_ratio\x18\x02 \x01(\x0b\x32\x1c.google.protobuf.DoubleValueB\x17\xfa\x42\x14\x12\x12\x19\x00\x00\x00\x00\x00\x00\x08@)\x00\x00\x00\x00\x00\x00\xf0?\x1aZ\n\"TypedExtensionProtocolOptionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12#\n\x05value\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any:\x02\x38\x01\"W\n\rDiscoveryType\x12\n\n\x06STATIC\x10\x00\x12\x0e\n\nSTRICT_DNS\x10\x01\x12\x0f\n\x0bLOGICAL_DNS\x10\x02\x12\x07\n\x03\x45\x44S\x10\x03\x12\x10\n\x0cORIGINAL_DST\x10\x04\"\xa4\x01\n\x08LbPolicy\x12\x0f\n\x0bROUND_ROBIN\x10\x00\x12\x11\n\rLEAST_REQUEST\x10\x01\x12\r\n\tRING_HASH\x10\x02\x12\n\n\x06RANDOM\x10\x03\x12\n\n\x06MAGLEV\x10\x05\x12\x14\n\x10\x43LUSTER_PROVIDED\x10\x06\x12 \n\x1cLOAD_BALANCING_POLICY_CONFIG\x10\x07\"\x04\x08\x04\x10\x04*\x0fORIGINAL_DST_LB\"P\n\x0f\x44nsLookupFamily\x12\x08\n\x04\x41UTO\x10\x00\x12\x0b\n\x07V4_ONLY\x10\x01\x12\x0b\n\x07V6_ONLY\x10\x02\x12\x10\n\x0cV4_PREFERRED\x10\x03\x12\x07\n\x03\x41LL\x10\x04\"T\n\x18\x43lusterProtocolSelection\x12\x1b\n\x17USE_CONFIGURED_PROTOCOL\x10\x00\x12\x1b\n\x17USE_DOWNSTREAM_PROTOCOL\x10\x01:\x1b\x9a\xc5\x88\x1e\x16\n\x14\x65nvoy.api.v2.ClusterB\x18\n\x16\x63luster_discovery_typeB\x0b\n\tlb_configJ\x04\x08\x0c\x10\rJ\x04\x08\x0f\x10\x10J\x04\x08\x07\x10\x08J\x04\x08\x0b\x10\x0cJ\x04\x08#\x10$R\x05hostsR\x0btls_contextR\x1a\x65xtension_protocol_options\"\xba\x02\n\x13LoadBalancingPolicy\x12\x45\n\x08policies\x18\x01 \x03(\x0b\x32\x33.envoy.config.cluster.v3.LoadBalancingPolicy.Policy\x1a\xb2\x01\n\x06Policy\x12J\n\x16typed_extension_config\x18\x04 \x01(\x0b\x32*.envoy.config.core.v3.TypedExtensionConfig:.\x9a\xc5\x88\x1e)\n\'envoy.api.v2.LoadBalancingPolicy.PolicyJ\x04\x08\x02\x10\x03J\x04\x08\x01\x10\x02J\x04\x08\x03\x10\x04R\x06\x63onfigR\x04nameR\x0ctyped_config:\'\x9a\xc5\x88\x1e\"\n envoy.api.v2.LoadBalancingPolicy\"\xbf\x01\n\x19UpstreamConnectionOptions\x12\x39\n\rtcp_keepalive\x18\x01 \x01(\x0b\x32\".envoy.config.core.v3.TcpKeepalive\x12\x38\n0set_local_interface_name_on_upstream_connections\x18\x02 \x01(\x08:-\x9a\xc5\x88\x1e(\n&envoy.api.v2.UpstreamConnectionOptions\"h\n\x11TrackClusterStats\x12\x17\n\x0ftimeout_budgets\x18\x01 \x01(\x08\x12\x1e\n\x16request_response_sizes\x18\x02 \x01(\x08\x12\x1a\n\x12per_endpoint_stats\x18\x03 \x01(\x08\x42\x89\x01\n%io.envoyproxy.envoy.config.cluster.v3B\x0c\x43lusterProtoP\x01ZHgithub.com/envoyproxy/go-control-plane/envoy/config/cluster/v3;clusterv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.config.cluster.v3.cluster_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n%io.envoyproxy.envoy.config.cluster.v3B\014ClusterProtoP\001ZHgithub.com/envoyproxy/go-control-plane/envoy/config/cluster/v3;clusterv3\272\200\310\321\006\002\020\002'
  _CLUSTER_TRANSPORTSOCKETMATCH.fields_by_name['name']._options = None
  _CLUSTER_TRANSPORTSOCKETMATCH.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _CLUSTER_TRANSPORTSOCKETMATCH._options = None
  _CLUSTER_TRANSPORTSOCKETMATCH._serialized_options = b'\232\305\210\036+\n)envoy.api.v2.Cluster.TransportSocketMatch'
  _CLUSTER_CUSTOMCLUSTERTYPE.fields_by_name['name']._options = None
  _CLUSTER_CUSTOMCLUSTERTYPE.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _CLUSTER_CUSTOMCLUSTERTYPE._options = None
  _CLUSTER_CUSTOMCLUSTERTYPE._serialized_options = b'\232\305\210\036(\n&envoy.api.v2.Cluster.CustomClusterType'
  _CLUSTER_EDSCLUSTERCONFIG._options = None
  _CLUSTER_EDSCLUSTERCONFIG._serialized_options = b'\232\305\210\036\'\n%envoy.api.v2.Cluster.EdsClusterConfig'
  _CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR.fields_by_name['fallback_policy']._options = None
  _CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR.fields_by_name['fallback_policy']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR._options = None
  _CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR._serialized_options = b'\232\305\210\0366\n4envoy.api.v2.Cluster.LbSubsetConfig.LbSubsetSelector'
  _CLUSTER_LBSUBSETCONFIG.fields_by_name['fallback_policy']._options = None
  _CLUSTER_LBSUBSETCONFIG.fields_by_name['fallback_policy']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER_LBSUBSETCONFIG.fields_by_name['metadata_fallback_policy']._options = None
  _CLUSTER_LBSUBSETCONFIG.fields_by_name['metadata_fallback_policy']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER_LBSUBSETCONFIG._options = None
  _CLUSTER_LBSUBSETCONFIG._serialized_options = b'\232\305\210\036%\n#envoy.api.v2.Cluster.LbSubsetConfig'
  _CLUSTER_LEASTREQUESTLBCONFIG.fields_by_name['choice_count']._options = None
  _CLUSTER_LEASTREQUESTLBCONFIG.fields_by_name['choice_count']._serialized_options = b'\372B\004*\002(\002'
  _CLUSTER_LEASTREQUESTLBCONFIG._options = None
  _CLUSTER_LEASTREQUESTLBCONFIG._serialized_options = b'\232\305\210\036+\n)envoy.api.v2.Cluster.LeastRequestLbConfig'
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['minimum_ring_size']._options = None
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['minimum_ring_size']._serialized_options = b'\372B\0072\005\030\200\200\200\004'
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['hash_function']._options = None
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['hash_function']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['maximum_ring_size']._options = None
  _CLUSTER_RINGHASHLBCONFIG.fields_by_name['maximum_ring_size']._serialized_options = b'\372B\0072\005\030\200\200\200\004'
  _CLUSTER_RINGHASHLBCONFIG._options = None
  _CLUSTER_RINGHASHLBCONFIG._serialized_options = b'\232\305\210\036\'\n%envoy.api.v2.Cluster.RingHashLbConfig'
  _CLUSTER_MAGLEVLBCONFIG.fields_by_name['table_size']._options = None
  _CLUSTER_MAGLEVLBCONFIG.fields_by_name['table_size']._serialized_options = b'\372B\0072\005\030\313\226\261\002'
  _CLUSTER_ORIGINALDSTLBCONFIG.fields_by_name['upstream_port_override']._options = None
  _CLUSTER_ORIGINALDSTLBCONFIG.fields_by_name['upstream_port_override']._serialized_options = b'\372B\006*\004\030\377\377\003'
  _CLUSTER_ORIGINALDSTLBCONFIG._options = None
  _CLUSTER_ORIGINALDSTLBCONFIG._serialized_options = b'\232\305\210\036*\n(envoy.api.v2.Cluster.OriginalDstLbConfig'
  _CLUSTER_COMMONLBCONFIG_ZONEAWARELBCONFIG._options = None
  _CLUSTER_COMMONLBCONFIG_ZONEAWARELBCONFIG._serialized_options = b'\232\305\210\0367\n5envoy.api.v2.Cluster.CommonLbConfig.ZoneAwareLbConfig'
  _CLUSTER_COMMONLBCONFIG_LOCALITYWEIGHTEDLBCONFIG._options = None
  _CLUSTER_COMMONLBCONFIG_LOCALITYWEIGHTEDLBCONFIG._serialized_options = b'\232\305\210\036>\n<envoy.api.v2.Cluster.CommonLbConfig.LocalityWeightedLbConfig'
  _CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG.fields_by_name['hash_balance_factor']._options = None
  _CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG.fields_by_name['hash_balance_factor']._serialized_options = b'\372B\004*\002(d'
  _CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG._options = None
  _CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG._serialized_options = b'\232\305\210\036?\n=envoy.api.v2.Cluster.CommonLbConfig.ConsistentHashingLbConfig'
  _CLUSTER_COMMONLBCONFIG._options = None
  _CLUSTER_COMMONLBCONFIG._serialized_options = b'\232\305\210\036%\n#envoy.api.v2.Cluster.CommonLbConfig'
  _CLUSTER_REFRESHRATE.fields_by_name['base_interval']._options = None
  _CLUSTER_REFRESHRATE.fields_by_name['base_interval']._serialized_options = b'\372B\013\252\001\010\010\001*\004\020\300\204='
  _CLUSTER_REFRESHRATE.fields_by_name['max_interval']._options = None
  _CLUSTER_REFRESHRATE.fields_by_name['max_interval']._serialized_options = b'\372B\t\252\001\006*\004\020\300\204='
  _CLUSTER_REFRESHRATE._options = None
  _CLUSTER_REFRESHRATE._serialized_options = b'\232\305\210\036\"\n envoy.api.v2.Cluster.RefreshRate'
  _CLUSTER_PRECONNECTPOLICY.fields_by_name['per_upstream_preconnect_ratio']._options = None
  _CLUSTER_PRECONNECTPOLICY.fields_by_name['per_upstream_preconnect_ratio']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\010@)\000\000\000\000\000\000\360?'
  _CLUSTER_PRECONNECTPOLICY.fields_by_name['predictive_preconnect_ratio']._options = None
  _CLUSTER_PRECONNECTPOLICY.fields_by_name['predictive_preconnect_ratio']._serialized_options = b'\372B\024\022\022\031\000\000\000\000\000\000\010@)\000\000\000\000\000\000\360?'
  _CLUSTER_TYPEDEXTENSIONPROTOCOLOPTIONSENTRY._options = None
  _CLUSTER_TYPEDEXTENSIONPROTOCOLOPTIONSENTRY._serialized_options = b'8\001'
  _CLUSTER.fields_by_name['name']._options = None
  _CLUSTER.fields_by_name['name']._serialized_options = b'\372B\004r\002\020\001'
  _CLUSTER.fields_by_name['alt_stat_name']._options = None
  _CLUSTER.fields_by_name['alt_stat_name']._serialized_options = b'\362\230\376\217\005\024\n\022observability_name'
  _CLUSTER.fields_by_name['type']._options = None
  _CLUSTER.fields_by_name['type']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER.fields_by_name['connect_timeout']._options = None
  _CLUSTER.fields_by_name['connect_timeout']._serialized_options = b'\372B\005\252\001\002*\000'
  _CLUSTER.fields_by_name['per_connection_buffer_limit_bytes']._options = None
  _CLUSTER.fields_by_name['per_connection_buffer_limit_bytes']._serialized_options = b'\212\223\267*\002\020\001'
  _CLUSTER.fields_by_name['lb_policy']._options = None
  _CLUSTER.fields_by_name['lb_policy']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER.fields_by_name['max_requests_per_connection']._options = None
  _CLUSTER.fields_by_name['max_requests_per_connection']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['upstream_http_protocol_options']._options = None
  _CLUSTER.fields_by_name['upstream_http_protocol_options']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['common_http_protocol_options']._options = None
  _CLUSTER.fields_by_name['common_http_protocol_options']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['http_protocol_options']._options = None
  _CLUSTER.fields_by_name['http_protocol_options']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['http2_protocol_options']._options = None
  _CLUSTER.fields_by_name['http2_protocol_options']._serialized_options = b'\030\001\212\223\267*\002\020\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['dns_refresh_rate']._options = None
  _CLUSTER.fields_by_name['dns_refresh_rate']._serialized_options = b'\372B\t\252\001\006*\004\020\300\204='
  _CLUSTER.fields_by_name['dns_lookup_family']._options = None
  _CLUSTER.fields_by_name['dns_lookup_family']._serialized_options = b'\372B\005\202\001\002\020\001'
  _CLUSTER.fields_by_name['dns_resolvers']._options = None
  _CLUSTER.fields_by_name['dns_resolvers']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['use_tcp_for_dns_lookups']._options = None
  _CLUSTER.fields_by_name['use_tcp_for_dns_lookups']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['dns_resolution_config']._options = None
  _CLUSTER.fields_by_name['dns_resolution_config']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['cleanup_interval']._options = None
  _CLUSTER.fields_by_name['cleanup_interval']._serialized_options = b'\372B\005\252\001\002*\000'
  _CLUSTER.fields_by_name['protocol_selection']._options = None
  _CLUSTER.fields_by_name['protocol_selection']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER.fields_by_name['track_timeout_budgets']._options = None
  _CLUSTER.fields_by_name['track_timeout_budgets']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CLUSTER._options = None
  _CLUSTER._serialized_options = b'\232\305\210\036\026\n\024envoy.api.v2.Cluster'
  _LOADBALANCINGPOLICY_POLICY._options = None
  _LOADBALANCINGPOLICY_POLICY._serialized_options = b'\232\305\210\036)\n\'envoy.api.v2.LoadBalancingPolicy.Policy'
  _LOADBALANCINGPOLICY._options = None
  _LOADBALANCINGPOLICY._serialized_options = b'\232\305\210\036\"\n envoy.api.v2.LoadBalancingPolicy'
  _UPSTREAMCONNECTIONOPTIONS._options = None
  _UPSTREAMCONNECTIONOPTIONS._serialized_options = b'\232\305\210\036(\n&envoy.api.v2.UpstreamConnectionOptions'
  _globals['_CLUSTERCOLLECTION']._serialized_start=923
  _globals['_CLUSTERCOLLECTION']._serialized_end=989
  _globals['_CLUSTER']._serialized_start=992
  _globals['_CLUSTER']._serialized_end=9753
  _globals['_CLUSTER_TRANSPORTSOCKETMATCH']._serialized_start=4643
  _globals['_CLUSTER_TRANSPORTSOCKETMATCH']._serialized_end=4843
  _globals['_CLUSTER_CUSTOMCLUSTERTYPE']._serialized_start=4846
  _globals['_CLUSTER_CUSTOMCLUSTERTYPE']._serialized_end=4979
  _globals['_CLUSTER_EDSCLUSTERCONFIG']._serialized_start=4982
  _globals['_CLUSTER_EDSCLUSTERCONFIG']._serialized_end=5124
  _globals['_CLUSTER_LBSUBSETCONFIG']._serialized_start=5127
  _globals['_CLUSTER_LBSUBSETCONFIG']._serialized_end=6240
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR']._serialized_start=5625
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR']._serialized_end=6036
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR_LBSUBSETSELECTORFALLBACKPOLICY']._serialized_start=5854
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETSELECTOR_LBSUBSETSELECTORFALLBACKPOLICY']._serialized_end=5975
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETFALLBACKPOLICY']._serialized_start=6038
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETFALLBACKPOLICY']._serialized_end=6117
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETMETADATAFALLBACKPOLICY']._serialized_start=6119
  _globals['_CLUSTER_LBSUBSETCONFIG_LBSUBSETMETADATAFALLBACKPOLICY']._serialized_end=6196
  _globals['_CLUSTER_SLOWSTARTCONFIG']._serialized_start=6243
  _globals['_CLUSTER_SLOWSTARTCONFIG']._serialized_end=6423
  _globals['_CLUSTER_ROUNDROBINLBCONFIG']._serialized_start=6425
  _globals['_CLUSTER_ROUNDROBINLBCONFIG']._serialized_end=6522
  _globals['_CLUSTER_LEASTREQUESTLBCONFIG']._serialized_start=6525
  _globals['_CLUSTER_LEASTREQUESTLBCONFIG']._serialized_end=6801
  _globals['_CLUSTER_RINGHASHLBCONFIG']._serialized_start=6804
  _globals['_CLUSTER_RINGHASHLBCONFIG']._serialized_end=7157
  _globals['_CLUSTER_RINGHASHLBCONFIG_HASHFUNCTION']._serialized_start=7059
  _globals['_CLUSTER_RINGHASHLBCONFIG_HASHFUNCTION']._serialized_end=7105
  _globals['_CLUSTER_MAGLEVLBCONFIG']._serialized_start=7159
  _globals['_CLUSTER_MAGLEVLBCONFIG']._serialized_end=7237
  _globals['_CLUSTER_ORIGINALDSTLBCONFIG']._serialized_start=7240
  _globals['_CLUSTER_ORIGINALDSTLBCONFIG']._serialized_end=7493
  _globals['_CLUSTER_COMMONLBCONFIG']._serialized_start=7496
  _globals['_CLUSTER_COMMONLBCONFIG']._serialized_end=8698
  _globals['_CLUSTER_COMMONLBCONFIG_ZONEAWARELBCONFIG']._serialized_start=8109
  _globals['_CLUSTER_COMMONLBCONFIG_ZONEAWARELBCONFIG']._serialized_end=8326
  _globals['_CLUSTER_COMMONLBCONFIG_LOCALITYWEIGHTEDLBCONFIG']._serialized_start=8328
  _globals['_CLUSTER_COMMONLBCONFIG_LOCALITYWEIGHTEDLBCONFIG']._serialized_end=8423
  _globals['_CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG']._serialized_start=8426
  _globals['_CLUSTER_COMMONLBCONFIG_CONSISTENTHASHINGLBCONFIG']._serialized_end=8625
  _globals['_CLUSTER_REFRESHRATE']._serialized_start=8701
  _globals['_CLUSTER_REFRESHRATE']._serialized_end=8884
  _globals['_CLUSTER_PRECONNECTPOLICY']._serialized_start=8887
  _globals['_CLUSTER_PRECONNECTPOLICY']._serialized_end=9091
  _globals['_CLUSTER_TYPEDEXTENSIONPROTOCOLOPTIONSENTRY']._serialized_start=9093
  _globals['_CLUSTER_TYPEDEXTENSIONPROTOCOLOPTIONSENTRY']._serialized_end=9183
  _globals['_CLUSTER_DISCOVERYTYPE']._serialized_start=9185
  _globals['_CLUSTER_DISCOVERYTYPE']._serialized_end=9272
  _globals['_CLUSTER_LBPOLICY']._serialized_start=9275
  _globals['_CLUSTER_LBPOLICY']._serialized_end=9439
  _globals['_CLUSTER_DNSLOOKUPFAMILY']._serialized_start=9441
  _globals['_CLUSTER_DNSLOOKUPFAMILY']._serialized_end=9521
  _globals['_CLUSTER_CLUSTERPROTOCOLSELECTION']._serialized_start=9523
  _globals['_CLUSTER_CLUSTERPROTOCOLSELECTION']._serialized_end=9607
  _globals['_LOADBALANCINGPOLICY']._serialized_start=9756
  _globals['_LOADBALANCINGPOLICY']._serialized_end=10070
  _globals['_LOADBALANCINGPOLICY_POLICY']._serialized_start=9851
  _globals['_LOADBALANCINGPOLICY_POLICY']._serialized_end=10029
  _globals['_UPSTREAMCONNECTIONOPTIONS']._serialized_start=10073
  _globals['_UPSTREAMCONNECTIONOPTIONS']._serialized_end=10264
  _globals['_TRACKCLUSTERSTATS']._serialized_start=10266
  _globals['_TRACKCLUSTERSTATS']._serialized_end=10370
# @@protoc_insertion_point(module_scope)
