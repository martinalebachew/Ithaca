# Bridge.py
# (C) Martin Alebachew, 2023

import python_bridge.interface_pb2 as interface
from Packets import HostToCardPacket, CardToHostPacket
from Shared import INSTRUCTIONS
from Utils import hexify, lookupResponse
from ATR import ATRInformation


# TODO: Generalize packet classes, do conversions in report code

def buildCommand(packet) -> interface.CommandPacket:
  command = interface.CommandPacket()
  command.pcap_index = int(packet.no)
  
  command.cla = packet.cla[0]
  command.ins = packet.ins[0]
  command.p1 = packet.p1[0]
  command.p2 = packet.p2[0]
  
  if len(packet.lc) > 0:
    command.lc = packet.lc[0]
    
  if len(packet.le) > 0:
    command.le = packet.le[0]
  
  if len(packet.data) > 0:
    command.data = packet.data
  
  # TODO: Avoid duplication with report
  if hexify(packet.ins) in INSTRUCTIONS.keys():
    command.is_known_command = True
    command.description = INSTRUCTIONS[hexify(packet.ins)] + (" (PROPRIETARY)" if packet.cla != b'\x00' else " (ISO/IEC 7816)")
  else:
    command.is_known_command = False
  
  return command


def buildResponse(packet) -> interface.ResponsePacket:
  response = interface.ResponsePacket()
  
  response.pcap_index = int(packet.no)
  
  if len(packet.data) > 0:
    response.data = packet.data
    
  response.sw1 = packet.sw1[0]
  response.sw2 = packet.sw2[0]
  
  response.description = description = lookupResponse(packet.sw1, packet.sw2)
  response.status = description[description.find("[") + 1:description.find("]")] if description else "Error"

  return response


def buildATR(packet) -> interface.ATRResponse:
  atr = interface.ATRResponse()
  
  if packet.data != "":
    info = ATRInformation(packet)
    atr.raw_atr = packet.data
    
    atr.chip = info.chip
    atr.standard = info.standard
    atr.file_structure = info.file_structure
    atr.software_issuer = info.software_issuer
    atr.software_version = info.software_version
    atr.lower_serial = info.lower_serial
  
  return atr


def encodePackets(packets) -> bytes:
  response = interface.PcapParseResponse()
  response.status = True
  
  response.atr_response.CopyFrom(buildATR(packets[0]))
  
  # TODO: Allow no-ATR / not first
  for packet in packets[1:]:
    if isinstance(packet, HostToCardPacket):
      response.commands.append(buildCommand(packet))
    elif isinstance(packet, CardToHostPacket):
      response.responses.append(buildResponse(packet))      
    else:
      raise ValueError("Unknown packet.")
  
  return response.SerializeToString()


def encodeParsingError() -> bytes:
  response = interface.PcapParseResponse()
  response.status = False
  return response.SerializeToString()
