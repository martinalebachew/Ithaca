# Bridge.py
# (C) Martin Alebachew, 2023

from typing import List
from ATR import ATRInformation
from Datagrams import Command, Response
from Utils import get_command_notes, get_response_notes
import python_bridge.interface_pb2 as interface


def build_command(datagram: Command) -> interface.Command:
    command = interface.Command()
    command.pcap_index = datagram.index

    command.cla = datagram.cla
    command.ins = datagram.ins
    command.p1 = datagram.p1
    command.p2 = datagram.p2

    if datagram.lc is not None:
        command.lc = datagram.lc
        
    if datagram.le is not None:
        command.le = datagram.le
    
    if datagram.data is not None:
        command.data = datagram.data

    (found, notes) = get_command_notes(datagram)
    command.is_known_command = found
    command.description = notes

    return command


def build_response(datagram: Response) -> interface.Response:
    response = interface.Response()

    response.pcap_index = datagram.index
    response.sw1 = datagram.sw1
    response.sw2 = datagram.sw2

    if datagram.data is not None:
        response.data = datagram.data
    
    (response.status, response.description) = get_response_notes(datagram)

    return response


def build_atr(datagram: Response) -> interface.ATRResponse:
  atr = interface.ATRResponse()
  
  if datagram.data != "":
    info = ATRInformation(datagram)
    atr.raw_atr = datagram.data
    
    atr.chip = info.chip
    atr.standard = info.standard
    atr.file_structure = info.file_structure
    atr.software_issuer = info.software_issuer
    atr.software_version = info.software_version
    atr.lower_serial = info.lower_serial
  
  return atr


def encode_datagrams(datagrams: List[Command | Response]) -> bytes:
    response = interface.PcapParseResponse()
    response.status = True
    
    # TODO: Allow no-ATR / not first
    response.atr_response.CopyFrom(build_atr(datagrams[0]))
    
    for datagram in datagrams[1:]:
        if isinstance(datagram, Command):
            response.commands.append(build_command(datagram))
        elif isinstance(datagram, Response):
            response.responses.append(build_response(datagram))      
        else:
            raise TypeError("Unknown datagram type!")
    
    return response.SerializeToString()


def encode_parsing_error() -> bytes:
    response = interface.PcapParseResponse()
    response.status = False
    return response.SerializeToString()
