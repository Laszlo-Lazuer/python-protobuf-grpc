# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: exercise_addressbook.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1a\x65xercise_addressbook.proto\x12\x1c\x65xample.exercise_addressbook\x1a\x1fgoogle/protobuf/timestamp.proto\"\xaf\x02\n\x06Person\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\n\n\x02id\x18\x02 \x01(\x05\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12@\n\x06phones\x18\x04 \x03(\x0b\x32\x30.example.exercise_addressbook.Person.PhoneNumber\x12\x30\n\x0clast_updated\x18\x05 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x1a[\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x01(\t\x12<\n\x04type\x18\x02 \x01(\x0e\x32..example.exercise_addressbook.Person.PhoneType\"+\n\tPhoneType\x12\n\n\x06MOBILE\x10\x00\x12\x08\n\x04HOME\x10\x01\x12\x08\n\x04WORK\x10\x02\"C\n\x0b\x41\x64\x64ressBook\x12\x34\n\x06people\x18\x01 \x03(\x0b\x32$.example.exercise_addressbook.Personb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'exercise_addressbook_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _PERSON._serialized_start=94
  _PERSON._serialized_end=397
  _PERSON_PHONENUMBER._serialized_start=261
  _PERSON_PHONENUMBER._serialized_end=352
  _PERSON_PHONETYPE._serialized_start=354
  _PERSON_PHONETYPE._serialized_end=397
  _ADDRESSBOOK._serialized_start=399
  _ADDRESSBOOK._serialized_end=466
# @@protoc_insertion_point(module_scope)