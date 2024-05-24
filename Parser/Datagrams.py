# Datagrams.py
# (C) Martin Alebachew, 2023

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import PcapReader, raw
from typing import List, Tuple

# More information about URB:
# https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-usb.c
URB_TRANSFER_TYPE_OFFSET = 22
URB_ENDPOINT_OFFSET = 21
URB_ENDPOINT_DIRECTION_MASK = 0x80
URB_DIRECTION_IN = URB_ENDPOINT_DIRECTION_MASK
URB_DIRECTION_OUT = 0
URB_BULK = 0x03

# More information about USB CCID:
# https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-usb-ccid.c
CCID_LAYER_LENGTH = 10
CCID_MESSAGE_TYPE_OFFSET = 0
CCID_PC_TO_READER_XFR = 0x6f
CCID_READER_TO_PC_DATA = 0x80


class Command:
    def __init__(self, index: int, raw_data: bytes):
        self.index = index

        self.cla = raw_data[0]
        self.ins = raw_data[1]
        self.p1 = raw_data[2]
        self.p2 = raw_data[3]

        if len(raw_data) == 4:
            self.lc = self.data = self.le = None
        else:
            if raw_data[4] != 0:
                # Single-byte lc represents data length
                self.lc = raw_data[4]
                self.data = raw_data[5:5 + self.lc]
                self.le = raw_data[5 + self.lc:]
                self.le = self.le[0] if self.le else None
            else:
                # Two bytes at lc + 1 represent data length
                self.lc = int.from_bytes(raw_data[5:7], "little")
                self.data = raw_data[7:7 + self.lc]
                self.le = raw_data[7 + self.lc:]
                self.le = self.le[0] if self.le else None

            if self.lc and not self.data:
                # Treat a case where only le is passed
                self.le = self.lc
                self.lc = self.data = None


class Response:
    def __init__(self, index: int, raw_data: bytes):
        self.index = index
        self.data = raw_data[0:-2] if len(raw_data) > 2 else None

        self.sw1 = raw_data[-2]
        self.sw2 = raw_data[-1]


def is_datagram_relevant(ccid_layer: bytes) -> bool:
    if len(ccid_layer) <= CCID_LAYER_LENGTH:
        return False
    
    message_type = ccid_layer[CCID_MESSAGE_TYPE_OFFSET]
    return message_type in [CCID_READER_TO_PC_DATA, CCID_PC_TO_READER_XFR]


def urb_to_datagram(raw_data: bytes) -> Tuple[int, bytes]:
    # TODO: Test this parsing method on more operating systems and drivers.
    # This might not be generic enough.
    
    urb_length = int.from_bytes(raw_data[0:2], "little")
    urb_layer = raw_data[:urb_length]

    if urb_length < URB_TRANSFER_TYPE_OFFSET + 1:
        raise ValueError("Unable to fetch URB data!")
    
    if urb_layer[URB_TRANSFER_TYPE_OFFSET] == URB_BULK:
        ccid_layer = raw_data[urb_length:]

        if is_datagram_relevant(ccid_layer):
            urb_endpoint = urb_layer[URB_ENDPOINT_OFFSET]
            direction = urb_endpoint & URB_ENDPOINT_DIRECTION_MASK
            payload = ccid_layer[CCID_LAYER_LENGTH:]
            return (direction, payload)

    return (None, None)


def parse_datagrams(filename: str) -> List[Command | Response]:
    parsed_datagrams = []

    for (index, data) in enumerate(PcapReader(filename)):
        direction, raw_data = urb_to_datagram(raw(data))

        if direction == URB_DIRECTION_IN:
            parsed_datagrams.append(Response(index, raw_data))
        elif direction == URB_DIRECTION_OUT:
            parsed_datagrams.append(Command(index, raw_data))
        # TODO: Account for ATR

    return parsed_datagrams
