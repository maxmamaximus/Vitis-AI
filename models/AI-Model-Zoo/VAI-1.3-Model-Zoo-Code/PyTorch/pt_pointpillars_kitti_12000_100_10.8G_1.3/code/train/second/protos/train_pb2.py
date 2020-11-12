
# This code is based on: https://github.com/nutonomy/second.pytorch.git
# 
# MIT License
# Copyright (c) 2018 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: second/protos/train.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from second.protos import optimizer_pb2 as second_dot_protos_dot_optimizer__pb2
from second.protos import preprocess_pb2 as second_dot_protos_dot_preprocess__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='second/protos/train.proto',
  package='second.protos',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x19second/protos/train.proto\x12\rsecond.protos\x1a\x1dsecond/protos/optimizer.proto\x1a\x1esecond/protos/preprocess.proto\"\x92\x01\n\x0bRegularizer\x12\x36\n\x0el1_regularizer\x18\x01 \x01(\x0b\x32\x1c.second.protos.L1RegularizerH\x00\x12\x36\n\x0el2_regularizer\x18\x02 \x01(\x0b\x32\x1c.second.protos.L2RegularizerH\x00\x42\x13\n\x11regularizer_oneof\"\x1f\n\rL1Regularizer\x12\x0e\n\x06weight\x18\x01 \x01(\x02\"\x1f\n\rL2Regularizer\x12\x0e\n\x06weight\x18\x01 \x01(\x02\"\xc6\x02\n\x0bTrainConfig\x12+\n\toptimizer\x18\x01 \x01(\x0b\x32\x18.second.protos.Optimizer\x12$\n\x1cinter_op_parallelism_threads\x18\x03 \x01(\r\x12$\n\x1cintra_op_parallelism_threads\x18\x04 \x01(\r\x12\r\n\x05steps\x18\x05 \x01(\r\x12\x16\n\x0esteps_per_eval\x18\x06 \x01(\r\x12\x1d\n\x15save_checkpoints_secs\x18\x07 \x01(\r\x12\x1a\n\x12save_summary_steps\x18\x08 \x01(\r\x12\x1e\n\x16\x65nable_mixed_precision\x18\t \x01(\x08\x12\x19\n\x11loss_scale_factor\x18\n \x01(\x02\x12!\n\x19\x63lear_metrics_every_epoch\x18\x0b \x01(\x08\x62\x06proto3')
  ,
  dependencies=[second_dot_protos_dot_optimizer__pb2.DESCRIPTOR,second_dot_protos_dot_preprocess__pb2.DESCRIPTOR,])




_REGULARIZER = _descriptor.Descriptor(
  name='Regularizer',
  full_name='second.protos.Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='l1_regularizer', full_name='second.protos.Regularizer.l1_regularizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='l2_regularizer', full_name='second.protos.Regularizer.l2_regularizer', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='regularizer_oneof', full_name='second.protos.Regularizer.regularizer_oneof',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=108,
  serialized_end=254,
)


_L1REGULARIZER = _descriptor.Descriptor(
  name='L1Regularizer',
  full_name='second.protos.L1Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.L1Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=256,
  serialized_end=287,
)


_L2REGULARIZER = _descriptor.Descriptor(
  name='L2Regularizer',
  full_name='second.protos.L2Regularizer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='weight', full_name='second.protos.L2Regularizer.weight', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=289,
  serialized_end=320,
)


_TRAINCONFIG = _descriptor.Descriptor(
  name='TrainConfig',
  full_name='second.protos.TrainConfig',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='optimizer', full_name='second.protos.TrainConfig.optimizer', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='inter_op_parallelism_threads', full_name='second.protos.TrainConfig.inter_op_parallelism_threads', index=1,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='intra_op_parallelism_threads', full_name='second.protos.TrainConfig.intra_op_parallelism_threads', index=2,
      number=4, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps', full_name='second.protos.TrainConfig.steps', index=3,
      number=5, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='steps_per_eval', full_name='second.protos.TrainConfig.steps_per_eval', index=4,
      number=6, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='save_checkpoints_secs', full_name='second.protos.TrainConfig.save_checkpoints_secs', index=5,
      number=7, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='save_summary_steps', full_name='second.protos.TrainConfig.save_summary_steps', index=6,
      number=8, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='enable_mixed_precision', full_name='second.protos.TrainConfig.enable_mixed_precision', index=7,
      number=9, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='loss_scale_factor', full_name='second.protos.TrainConfig.loss_scale_factor', index=8,
      number=10, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='clear_metrics_every_epoch', full_name='second.protos.TrainConfig.clear_metrics_every_epoch', index=9,
      number=11, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=323,
  serialized_end=649,
)

_REGULARIZER.fields_by_name['l1_regularizer'].message_type = _L1REGULARIZER
_REGULARIZER.fields_by_name['l2_regularizer'].message_type = _L2REGULARIZER
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l1_regularizer'])
_REGULARIZER.fields_by_name['l1_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_REGULARIZER.oneofs_by_name['regularizer_oneof'].fields.append(
  _REGULARIZER.fields_by_name['l2_regularizer'])
_REGULARIZER.fields_by_name['l2_regularizer'].containing_oneof = _REGULARIZER.oneofs_by_name['regularizer_oneof']
_TRAINCONFIG.fields_by_name['optimizer'].message_type = second_dot_protos_dot_optimizer__pb2._OPTIMIZER
DESCRIPTOR.message_types_by_name['Regularizer'] = _REGULARIZER
DESCRIPTOR.message_types_by_name['L1Regularizer'] = _L1REGULARIZER
DESCRIPTOR.message_types_by_name['L2Regularizer'] = _L2REGULARIZER
DESCRIPTOR.message_types_by_name['TrainConfig'] = _TRAINCONFIG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Regularizer = _reflection.GeneratedProtocolMessageType('Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _REGULARIZER,
  __module__ = 'second.protos.train_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.Regularizer)
  ))
_sym_db.RegisterMessage(Regularizer)

L1Regularizer = _reflection.GeneratedProtocolMessageType('L1Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _L1REGULARIZER,
  __module__ = 'second.protos.train_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.L1Regularizer)
  ))
_sym_db.RegisterMessage(L1Regularizer)

L2Regularizer = _reflection.GeneratedProtocolMessageType('L2Regularizer', (_message.Message,), dict(
  DESCRIPTOR = _L2REGULARIZER,
  __module__ = 'second.protos.train_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.L2Regularizer)
  ))
_sym_db.RegisterMessage(L2Regularizer)

TrainConfig = _reflection.GeneratedProtocolMessageType('TrainConfig', (_message.Message,), dict(
  DESCRIPTOR = _TRAINCONFIG,
  __module__ = 'second.protos.train_pb2'
  # @@protoc_insertion_point(class_scope:second.protos.TrainConfig)
  ))
_sym_db.RegisterMessage(TrainConfig)


# @@protoc_insertion_point(module_scope)
