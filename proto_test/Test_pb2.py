# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Test.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\nTest.proto\"\x18\n\x08send_msg\x12\x0c\n\x04send\x18\x01 \x01(\t\",\n\x0cresponse_msg\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x0b\n\x03msg\x18\x02 \x01(\t2\xbb\x01\n\rTest_Streamer\x12&\n\nOne_to_One\x12\t.send_msg\x1a\r.response_msg\x12)\n\x0bMany_to_One\x12\t.send_msg\x1a\r.response_msg(\x01\x12)\n\x0bOne_to_Many\x12\t.send_msg\x1a\r.response_msg0\x01\x12,\n\x0cMany_to_Many\x12\t.send_msg\x1a\r.response_msg(\x01\x30\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'Test_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_SEND_MSG']._serialized_start=14
  _globals['_SEND_MSG']._serialized_end=38
  _globals['_RESPONSE_MSG']._serialized_start=40
  _globals['_RESPONSE_MSG']._serialized_end=84
  _globals['_TEST_STREAMER']._serialized_start=87
  _globals['_TEST_STREAMER']._serialized_end=274
# @@protoc_insertion_point(module_scope)
