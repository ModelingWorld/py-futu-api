# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='Common.proto',
  package='Common',
  syntax='proto2',
  serialized_pb=_b('\n\x0c\x43ommon.proto\x12\x06\x43ommon\",\n\x08PacketID\x12\x0e\n\x06\x63onnID\x18\x01 \x02(\x04\x12\x10\n\x08serialNo\x18\x02 \x02(\r\"L\n\rProgramStatus\x12\'\n\x04type\x18\x01 \x02(\x0e\x32\x19.Common.ProgramStatusType\x12\x12\n\nstrExtDesc\x18\x02 \x01(\t*\xb6\x01\n\x07RetType\x12\x13\n\x0fRetType_Succeed\x10\x00\x12\x1b\n\x0eRetType_Failed\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fRetType_TimeOut\x10\x9c\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1f\n\x12RetType_DisConnect\x10\xb8\xfe\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fRetType_Unknown\x10\xf0\xfc\xff\xff\xff\xff\xff\xff\xff\x01\x12\x1c\n\x0fRetType_Invalid\x10\x8c\xfc\xff\xff\xff\xff\xff\xff\xff\x01*\x83\x01\n\rPacketEncAlgo\x12\x1b\n\x17PacketEncAlgo_FTAES_ECB\x10\x00\x12\x1f\n\x12PacketEncAlgo_None\x10\xff\xff\xff\xff\xff\xff\xff\xff\xff\x01\x12\x19\n\x15PacketEncAlgo_AES_ECB\x10\x01\x12\x19\n\x15PacketEncAlgo_AES_CBC\x10\x02*4\n\x08ProtoFmt\x12\x15\n\x11ProtoFmt_Protobuf\x10\x00\x12\x11\n\rProtoFmt_Json\x10\x01*\xf0\x03\n\x11ProgramStatusType\x12\x1a\n\x16ProgramStatusType_None\x10\x00\x12\x1c\n\x18ProgramStatusType_Loaded\x10\x01\x12\x1c\n\x18ProgramStatusType_Loging\x10\x02\x12\'\n#ProgramStatusType_NeedPicVerifyCode\x10\x03\x12)\n%ProgramStatusType_NeedPhoneVerifyCode\x10\x04\x12!\n\x1dProgramStatusType_LoginFailed\x10\x05\x12!\n\x1dProgramStatusType_ForceUpdate\x10\x06\x12*\n&ProgramStatusType_NessaryDataPreparing\x10\x07\x12(\n$ProgramStatusType_NessaryDataMissing\x10\x08\x12\'\n#ProgramStatusType_UnAgreeDisclaimer\x10\t\x12\x1b\n\x17ProgramStatusType_Ready\x10\n\x12!\n\x1dProgramStatusType_ForceLogout\x10\x0b\x12*\n&ProgramStatusType_DisclaimerPullFailed\x10\x0c\x42=\n\x13\x63om.futu.openapi.pbZ&github.com/futuopen/ftapi4go/pb/common')
)

_RETTYPE = _descriptor.EnumDescriptor(
  name='RetType',
  full_name='Common.RetType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='RetType_Succeed', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_Failed', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_TimeOut', index=2, number=-100,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_DisConnect', index=3, number=-200,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_Unknown', index=4, number=-400,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='RetType_Invalid', index=5, number=-500,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=149,
  serialized_end=331,
)
_sym_db.RegisterEnumDescriptor(_RETTYPE)

RetType = enum_type_wrapper.EnumTypeWrapper(_RETTYPE)
_PACKETENCALGO = _descriptor.EnumDescriptor(
  name='PacketEncAlgo',
  full_name='Common.PacketEncAlgo',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_FTAES_ECB', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_None', index=1, number=-1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_AES_ECB', index=2, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PacketEncAlgo_AES_CBC', index=3, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=334,
  serialized_end=465,
)
_sym_db.RegisterEnumDescriptor(_PACKETENCALGO)

PacketEncAlgo = enum_type_wrapper.EnumTypeWrapper(_PACKETENCALGO)
_PROTOFMT = _descriptor.EnumDescriptor(
  name='ProtoFmt',
  full_name='Common.ProtoFmt',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ProtoFmt_Protobuf', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProtoFmt_Json', index=1, number=1,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=467,
  serialized_end=519,
)
_sym_db.RegisterEnumDescriptor(_PROTOFMT)

ProtoFmt = enum_type_wrapper.EnumTypeWrapper(_PROTOFMT)
_PROGRAMSTATUSTYPE = _descriptor.EnumDescriptor(
  name='ProgramStatusType',
  full_name='Common.ProgramStatusType',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_None', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_Loaded', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_Loging', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_NeedPicVerifyCode', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_NeedPhoneVerifyCode', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_LoginFailed', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_ForceUpdate', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_NessaryDataPreparing', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_NessaryDataMissing', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_UnAgreeDisclaimer', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_Ready', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_ForceLogout', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='ProgramStatusType_DisclaimerPullFailed', index=12, number=12,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=522,
  serialized_end=1018,
)
_sym_db.RegisterEnumDescriptor(_PROGRAMSTATUSTYPE)

ProgramStatusType = enum_type_wrapper.EnumTypeWrapper(_PROGRAMSTATUSTYPE)
RetType_Succeed = 0
RetType_Failed = -1
RetType_TimeOut = -100
RetType_DisConnect = -200
RetType_Unknown = -400
RetType_Invalid = -500
PacketEncAlgo_FTAES_ECB = 0
PacketEncAlgo_None = -1
PacketEncAlgo_AES_ECB = 1
PacketEncAlgo_AES_CBC = 2
ProtoFmt_Protobuf = 0
ProtoFmt_Json = 1
ProgramStatusType_None = 0
ProgramStatusType_Loaded = 1
ProgramStatusType_Loging = 2
ProgramStatusType_NeedPicVerifyCode = 3
ProgramStatusType_NeedPhoneVerifyCode = 4
ProgramStatusType_LoginFailed = 5
ProgramStatusType_ForceUpdate = 6
ProgramStatusType_NessaryDataPreparing = 7
ProgramStatusType_NessaryDataMissing = 8
ProgramStatusType_UnAgreeDisclaimer = 9
ProgramStatusType_Ready = 10
ProgramStatusType_ForceLogout = 11
ProgramStatusType_DisclaimerPullFailed = 12



_PACKETID = _descriptor.Descriptor(
  name='PacketID',
  full_name='Common.PacketID',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='connID', full_name='Common.PacketID.connID', index=0,
      number=1, type=4, cpp_type=4, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='serialNo', full_name='Common.PacketID.serialNo', index=1,
      number=2, type=13, cpp_type=3, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=24,
  serialized_end=68,
)


_PROGRAMSTATUS = _descriptor.Descriptor(
  name='ProgramStatus',
  full_name='Common.ProgramStatus',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='type', full_name='Common.ProgramStatus.type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strExtDesc', full_name='Common.ProgramStatus.strExtDesc', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=70,
  serialized_end=146,
)

_PROGRAMSTATUS.fields_by_name['type'].enum_type = _PROGRAMSTATUSTYPE
DESCRIPTOR.message_types_by_name['PacketID'] = _PACKETID
DESCRIPTOR.message_types_by_name['ProgramStatus'] = _PROGRAMSTATUS
DESCRIPTOR.enum_types_by_name['RetType'] = _RETTYPE
DESCRIPTOR.enum_types_by_name['PacketEncAlgo'] = _PACKETENCALGO
DESCRIPTOR.enum_types_by_name['ProtoFmt'] = _PROTOFMT
DESCRIPTOR.enum_types_by_name['ProgramStatusType'] = _PROGRAMSTATUSTYPE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

PacketID = _reflection.GeneratedProtocolMessageType('PacketID', (_message.Message,), dict(
  DESCRIPTOR = _PACKETID,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:Common.PacketID)
  ))
_sym_db.RegisterMessage(PacketID)

ProgramStatus = _reflection.GeneratedProtocolMessageType('ProgramStatus', (_message.Message,), dict(
  DESCRIPTOR = _PROGRAMSTATUS,
  __module__ = 'Common_pb2'
  # @@protoc_insertion_point(class_scope:Common.ProgramStatus)
  ))
_sym_db.RegisterMessage(ProgramStatus)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\023com.futu.openapi.pbZ&github.com/futuopen/ftapi4go/pb/common'))
# @@protoc_insertion_point(module_scope)
