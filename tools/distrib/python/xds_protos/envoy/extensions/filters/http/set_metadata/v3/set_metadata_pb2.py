# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/extensions/filters/http/set_metadata/v3/set_metadata.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2
from envoy.annotations import deprecation_pb2 as envoy_dot_annotations_dot_deprecation__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from validate import validate_pb2 as validate_dot_validate__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n@envoy/extensions/filters/http/set_metadata/v3/set_metadata.proto\x12-envoy.extensions.filters.http.set_metadata.v3\x1a\x19google/protobuf/any.proto\x1a\x1cgoogle/protobuf/struct.proto\x1a#envoy/annotations/deprecation.proto\x1a\x1dudpa/annotations/status.proto\x1a\x17validate/validate.proto\"\x9b\x01\n\x08Metadata\x12#\n\x12metadata_namespace\x18\x01 \x01(\tB\x07\xfa\x42\x04r\x02\x10\x01\x12\x17\n\x0f\x61llow_overwrite\x18\x02 \x01(\x08\x12&\n\x05value\x18\x03 \x01(\x0b\x32\x17.google.protobuf.Struct\x12)\n\x0btyped_value\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any\"\xb1\x01\n\x06\x43onfig\x12\'\n\x12metadata_namespace\x18\x01 \x01(\tB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12\x33\n\x05value\x18\x02 \x01(\x0b\x32\x17.google.protobuf.StructB\x0b\x18\x01\x92\xc7\x86\xd8\x04\x03\x33.0\x12I\n\x08metadata\x18\x03 \x03(\x0b\x32\x37.envoy.extensions.filters.http.set_metadata.v3.MetadataB\xbe\x01\n;io.envoyproxy.envoy.extensions.filters.http.set_metadata.v3B\x10SetMetadataProtoP\x01Zcgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/set_metadata/v3;set_metadatav3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.extensions.filters.http.set_metadata.v3.set_metadata_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n;io.envoyproxy.envoy.extensions.filters.http.set_metadata.v3B\020SetMetadataProtoP\001Zcgithub.com/envoyproxy/go-control-plane/envoy/extensions/filters/http/set_metadata/v3;set_metadatav3\272\200\310\321\006\002\020\002'
  _METADATA.fields_by_name['metadata_namespace']._options = None
  _METADATA.fields_by_name['metadata_namespace']._serialized_options = b'\372B\004r\002\020\001'
  _CONFIG.fields_by_name['metadata_namespace']._options = None
  _CONFIG.fields_by_name['metadata_namespace']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _CONFIG.fields_by_name['value']._options = None
  _CONFIG.fields_by_name['value']._serialized_options = b'\030\001\222\307\206\330\004\0033.0'
  _globals['_METADATA']._serialized_start=266
  _globals['_METADATA']._serialized_end=421
  _globals['_CONFIG']._serialized_start=424
  _globals['_CONFIG']._serialized_end=601
# @@protoc_insertion_point(module_scope)
