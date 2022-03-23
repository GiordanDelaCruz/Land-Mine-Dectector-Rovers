# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: rover.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0brover.proto\"\"\n\nmapRequest\x12\x14\n\x0crover_number\x18\x01 \x01(\x05\"%\n\x0bmapResponse\x12\x16\n\x0einternal_array\x18\x01 \x03(\t\"#\n\x0bmoveRequest\x12\x14\n\x0crover_number\x18\x01 \x01(\x05\"%\n\x0cmoveResponse\x12\x15\n\rmove_sequence\x18\x01 \x01(\t\"\x16\n\x14mineSerialNumRequest\"*\n\x15mineSerialNumResponse\x12\x11\n\tserialNum\x18\x01 \x01(\t\"\x1c\n\x1aroverSuccessfulFlagRequest\"5\n\x1broverSuccessfulFlagResponse\x12\x16\n\x0esuccessfulFlag\x18\x01 \x01(\x08\"\x10\n\x0eminePinRequest\"#\n\x0fminePinResponse\x12\x10\n\x08mine_pin\x18\x01 \x01(\t2\xbc\x02\n\x0cRoverService\x12\x30\n\x11generate_map_list\x12\x0b.mapRequest\x1a\x0c.mapResponse\"\x00\x12.\n\rgetRoverMoves\x12\x0c.moveRequest\x1a\r.moveResponse\"\x00\x12\x41\n\x0eget_serial_num\x12\x15.mineSerialNumRequest\x1a\x16.mineSerialNumResponse\"\x00\x12R\n\x13get_successful_flag\x12\x1b.roverSuccessfulFlagRequest\x1a\x1c.roverSuccessfulFlagResponse\"\x00\x12\x33\n\x0cget_mine_pin\x12\x0f.minePinRequest\x1a\x10.minePinResponse\"\x00\x62\x06proto3')



_MAPREQUEST = DESCRIPTOR.message_types_by_name['mapRequest']
_MAPRESPONSE = DESCRIPTOR.message_types_by_name['mapResponse']
_MOVEREQUEST = DESCRIPTOR.message_types_by_name['moveRequest']
_MOVERESPONSE = DESCRIPTOR.message_types_by_name['moveResponse']
_MINESERIALNUMREQUEST = DESCRIPTOR.message_types_by_name['mineSerialNumRequest']
_MINESERIALNUMRESPONSE = DESCRIPTOR.message_types_by_name['mineSerialNumResponse']
_ROVERSUCCESSFULFLAGREQUEST = DESCRIPTOR.message_types_by_name['roverSuccessfulFlagRequest']
_ROVERSUCCESSFULFLAGRESPONSE = DESCRIPTOR.message_types_by_name['roverSuccessfulFlagResponse']
_MINEPINREQUEST = DESCRIPTOR.message_types_by_name['minePinRequest']
_MINEPINRESPONSE = DESCRIPTOR.message_types_by_name['minePinResponse']
mapRequest = _reflection.GeneratedProtocolMessageType('mapRequest', (_message.Message,), {
  'DESCRIPTOR' : _MAPREQUEST,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:mapRequest)
  })
_sym_db.RegisterMessage(mapRequest)

mapResponse = _reflection.GeneratedProtocolMessageType('mapResponse', (_message.Message,), {
  'DESCRIPTOR' : _MAPRESPONSE,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:mapResponse)
  })
_sym_db.RegisterMessage(mapResponse)

moveRequest = _reflection.GeneratedProtocolMessageType('moveRequest', (_message.Message,), {
  'DESCRIPTOR' : _MOVEREQUEST,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:moveRequest)
  })
_sym_db.RegisterMessage(moveRequest)

moveResponse = _reflection.GeneratedProtocolMessageType('moveResponse', (_message.Message,), {
  'DESCRIPTOR' : _MOVERESPONSE,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:moveResponse)
  })
_sym_db.RegisterMessage(moveResponse)

mineSerialNumRequest = _reflection.GeneratedProtocolMessageType('mineSerialNumRequest', (_message.Message,), {
  'DESCRIPTOR' : _MINESERIALNUMREQUEST,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:mineSerialNumRequest)
  })
_sym_db.RegisterMessage(mineSerialNumRequest)

mineSerialNumResponse = _reflection.GeneratedProtocolMessageType('mineSerialNumResponse', (_message.Message,), {
  'DESCRIPTOR' : _MINESERIALNUMRESPONSE,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:mineSerialNumResponse)
  })
_sym_db.RegisterMessage(mineSerialNumResponse)

roverSuccessfulFlagRequest = _reflection.GeneratedProtocolMessageType('roverSuccessfulFlagRequest', (_message.Message,), {
  'DESCRIPTOR' : _ROVERSUCCESSFULFLAGREQUEST,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:roverSuccessfulFlagRequest)
  })
_sym_db.RegisterMessage(roverSuccessfulFlagRequest)

roverSuccessfulFlagResponse = _reflection.GeneratedProtocolMessageType('roverSuccessfulFlagResponse', (_message.Message,), {
  'DESCRIPTOR' : _ROVERSUCCESSFULFLAGRESPONSE,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:roverSuccessfulFlagResponse)
  })
_sym_db.RegisterMessage(roverSuccessfulFlagResponse)

minePinRequest = _reflection.GeneratedProtocolMessageType('minePinRequest', (_message.Message,), {
  'DESCRIPTOR' : _MINEPINREQUEST,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:minePinRequest)
  })
_sym_db.RegisterMessage(minePinRequest)

minePinResponse = _reflection.GeneratedProtocolMessageType('minePinResponse', (_message.Message,), {
  'DESCRIPTOR' : _MINEPINRESPONSE,
  '__module__' : 'rover_pb2'
  # @@protoc_insertion_point(class_scope:minePinResponse)
  })
_sym_db.RegisterMessage(minePinResponse)

_ROVERSERVICE = DESCRIPTOR.services_by_name['RoverService']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _MAPREQUEST._serialized_start=15
  _MAPREQUEST._serialized_end=49
  _MAPRESPONSE._serialized_start=51
  _MAPRESPONSE._serialized_end=88
  _MOVEREQUEST._serialized_start=90
  _MOVEREQUEST._serialized_end=125
  _MOVERESPONSE._serialized_start=127
  _MOVERESPONSE._serialized_end=164
  _MINESERIALNUMREQUEST._serialized_start=166
  _MINESERIALNUMREQUEST._serialized_end=188
  _MINESERIALNUMRESPONSE._serialized_start=190
  _MINESERIALNUMRESPONSE._serialized_end=232
  _ROVERSUCCESSFULFLAGREQUEST._serialized_start=234
  _ROVERSUCCESSFULFLAGREQUEST._serialized_end=262
  _ROVERSUCCESSFULFLAGRESPONSE._serialized_start=264
  _ROVERSUCCESSFULFLAGRESPONSE._serialized_end=317
  _MINEPINREQUEST._serialized_start=319
  _MINEPINREQUEST._serialized_end=335
  _MINEPINRESPONSE._serialized_start=337
  _MINEPINRESPONSE._serialized_end=372
  _ROVERSERVICE._serialized_start=375
  _ROVERSERVICE._serialized_end=691
# @@protoc_insertion_point(module_scope)
