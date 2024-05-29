# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: envoy/service/auth/v3/attribute_context.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from envoy.config.core.v3 import address_pb2 as envoy_dot_config_dot_core_dot_v3_dot_address__pb2
from envoy.config.core.v3 import base_pb2 as envoy_dot_config_dot_core_dot_v3_dot_base__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from udpa.annotations import status_pb2 as udpa_dot_annotations_dot_status__pb2
from udpa.annotations import versioning_pb2 as udpa_dot_annotations_dot_versioning__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n-envoy/service/auth/v3/attribute_context.proto\x12\x15\x65nvoy.service.auth.v3\x1a\"envoy/config/core/v3/address.proto\x1a\x1f\x65nvoy/config/core/v3/base.proto\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1dudpa/annotations/status.proto\x1a!udpa/annotations/versioning.proto\"\xbe\x0b\n\x10\x41ttributeContext\x12<\n\x06source\x18\x01 \x01(\x0b\x32,.envoy.service.auth.v3.AttributeContext.Peer\x12\x41\n\x0b\x64\x65stination\x18\x02 \x01(\x0b\x32,.envoy.service.auth.v3.AttributeContext.Peer\x12@\n\x07request\x18\x04 \x01(\x0b\x32/.envoy.service.auth.v3.AttributeContext.Request\x12Z\n\x12\x63ontext_extensions\x18\n \x03(\x0b\x32>.envoy.service.auth.v3.AttributeContext.ContextExtensionsEntry\x12\x38\n\x10metadata_context\x18\x0b \x01(\x0b\x32\x1e.envoy.config.core.v3.Metadata\x12>\n\x16route_metadata_context\x18\r \x01(\x0b\x32\x1e.envoy.config.core.v3.Metadata\x12G\n\x0btls_session\x18\x0c \x01(\x0b\x32\x32.envoy.service.auth.v3.AttributeContext.TLSSession\x1a\x9c\x02\n\x04Peer\x12.\n\x07\x61\x64\x64ress\x18\x01 \x01(\x0b\x32\x1d.envoy.config.core.v3.Address\x12\x0f\n\x07service\x18\x02 \x01(\t\x12H\n\x06labels\x18\x03 \x03(\x0b\x32\x38.envoy.service.auth.v3.AttributeContext.Peer.LabelsEntry\x12\x11\n\tprincipal\x18\x04 \x01(\t\x12\x13\n\x0b\x63\x65rtificate\x18\x05 \x01(\t\x1a-\n\x0bLabelsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:2\x9a\xc5\x88\x1e-\n+envoy.service.auth.v2.AttributeContext.Peer\x1a\xad\x01\n\x07Request\x12(\n\x04time\x18\x01 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x41\n\x04http\x18\x02 \x01(\x0b\x32\x33.envoy.service.auth.v3.AttributeContext.HttpRequest:5\x9a\xc5\x88\x1e\x30\n.envoy.service.auth.v2.AttributeContext.Request\x1a\xf4\x02\n\x0bHttpRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x0e\n\x06method\x18\x02 \x01(\t\x12Q\n\x07headers\x18\x03 \x03(\x0b\x32@.envoy.service.auth.v3.AttributeContext.HttpRequest.HeadersEntry\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\x0c\n\x04host\x18\x05 \x01(\t\x12\x0e\n\x06scheme\x18\x06 \x01(\t\x12\r\n\x05query\x18\x07 \x01(\t\x12\x10\n\x08\x66ragment\x18\x08 \x01(\t\x12\x0c\n\x04size\x18\t \x01(\x03\x12\x10\n\x08protocol\x18\n \x01(\t\x12\x0c\n\x04\x62ody\x18\x0b \x01(\t\x12\x10\n\x08raw_body\x18\x0c \x01(\x0c\x1a.\n\x0cHeadersEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:9\x9a\xc5\x88\x1e\x34\n2envoy.service.auth.v2.AttributeContext.HttpRequest\x1a\x19\n\nTLSSession\x12\x0b\n\x03sni\x18\x01 \x01(\t\x1a\x38\n\x16\x43ontextExtensionsEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01:-\x9a\xc5\x88\x1e(\n&envoy.service.auth.v2.AttributeContextB\x8b\x01\n#io.envoyproxy.envoy.service.auth.v3B\x15\x41ttributeContextProtoP\x01ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v3;authv3\xba\x80\xc8\xd1\x06\x02\x10\x02\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'envoy.service.auth.v3.attribute_context_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n#io.envoyproxy.envoy.service.auth.v3B\025AttributeContextProtoP\001ZCgithub.com/envoyproxy/go-control-plane/envoy/service/auth/v3;authv3\272\200\310\321\006\002\020\002'
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._options = None
  _ATTRIBUTECONTEXT_PEER_LABELSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT_PEER._options = None
  _ATTRIBUTECONTEXT_PEER._serialized_options = b'\232\305\210\036-\n+envoy.service.auth.v2.AttributeContext.Peer'
  _ATTRIBUTECONTEXT_REQUEST._options = None
  _ATTRIBUTECONTEXT_REQUEST._serialized_options = b'\232\305\210\0360\n.envoy.service.auth.v2.AttributeContext.Request'
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._options = None
  _ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT_HTTPREQUEST._options = None
  _ATTRIBUTECONTEXT_HTTPREQUEST._serialized_options = b'\232\305\210\0364\n2envoy.service.auth.v2.AttributeContext.HttpRequest'
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._options = None
  _ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY._serialized_options = b'8\001'
  _ATTRIBUTECONTEXT._options = None
  _ATTRIBUTECONTEXT._serialized_options = b'\232\305\210\036(\n&envoy.service.auth.v2.AttributeContext'
  _globals['_ATTRIBUTECONTEXT']._serialized_start=241
  _globals['_ATTRIBUTECONTEXT']._serialized_end=1711
  _globals['_ATTRIBUTECONTEXT_PEER']._serialized_start=744
  _globals['_ATTRIBUTECONTEXT_PEER']._serialized_end=1028
  _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._serialized_start=931
  _globals['_ATTRIBUTECONTEXT_PEER_LABELSENTRY']._serialized_end=976
  _globals['_ATTRIBUTECONTEXT_REQUEST']._serialized_start=1031
  _globals['_ATTRIBUTECONTEXT_REQUEST']._serialized_end=1204
  _globals['_ATTRIBUTECONTEXT_HTTPREQUEST']._serialized_start=1207
  _globals['_ATTRIBUTECONTEXT_HTTPREQUEST']._serialized_end=1579
  _globals['_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY']._serialized_start=1474
  _globals['_ATTRIBUTECONTEXT_HTTPREQUEST_HEADERSENTRY']._serialized_end=1520
  _globals['_ATTRIBUTECONTEXT_TLSSESSION']._serialized_start=1581
  _globals['_ATTRIBUTECONTEXT_TLSSESSION']._serialized_end=1606
  _globals['_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY']._serialized_start=1608
  _globals['_ATTRIBUTECONTEXT_CONTEXTEXTENSIONSENTRY']._serialized_end=1664
# @@protoc_insertion_point(module_scope)
