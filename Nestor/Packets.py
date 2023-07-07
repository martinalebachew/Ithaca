# Packets.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)

from scapy.all import *
from Utils import hexify


class HostToCardPacket:
    def __init__(self, index, rawData):
        self.no = str(index + 1)

        # Note: using single-byte arrays to disable int conversion
        self.cla = rawData[0:1]
        self.ins = rawData[1:2]
        self.p1 = rawData[2:3]
        self.p2 = rawData[3:4]

        if len(rawData) == 4:
            self.lc = self.data = self.le = ""
        else:
            if rawData[4] != 0:
                # Single-byte lc represents data length
                self.lc = rawData[4:5]
                self.data = rawData[5:5 + int.from_bytes(self.lc, "little")]
                self.le = rawData[5 + int.from_bytes(self.lc, "little"):]

            else:
                # Two bytes at lc + 1 represent data length
                self.lc = rawData[5:7]
                self.data = rawData[7:7 + int.from_bytes(self.lc, "little")]
                self.le = rawData[7 + int.from_bytes(self.lc, "little"):]

            if self.lc and not self.data:
                # Treat a case where only le is passed
                self.le = self.lc
                self.lc = self.data = ""
            else:
                # Make sure le is properly initialized
                self.le = self.le if self.le else ""

        # Format data for the report
        self.serialized = [self.no, "H>C", self.cla, self.ins, self.p1, self.p2, self.lc, self.data, self.le]
        for i in range(2, len(self.serialized)):
            self.serialized[i] = hexify(self.serialized[i])


class CardToHostPacket:
    def __init__(self, index, rawData):
        self.no = str(index + 1)
        self.data = rawData[0:-2] if len(rawData) > 2 else ""

        # Note: using single-byte arrays to disable int conversion
        self.sw1 = rawData[-2:-1]
        self.sw2 = rawData[-1:]

        # Format data for the report
        self.serialized = [self.no, "C>H", self.data, self.sw1, self.sw2]
        for i in range(2, len(self.serialized)):
            self.serialized[i] = hexify(self.serialized[i])


def sanitize(rawData):
    urbLength = int.from_bytes(rawData[0:2], "little")
    urbLayer = rawData[:urbLength]

    if urbLength < 23:  # Invalid URB header
        raise "Unable to fetch URB data!"
    elif urbLayer[22] == 0x03:  # Make sure packet type is URB_BULK
        rawData = rawData[urbLength + 10:]  # Throw URB and CCID layers
        if len(rawData) > 0:
            # Direction flag: MSB on for IN, off for OUT
            return "IN" if urbLayer[21] >= 80 else "OUT", rawData

    return None, None


def parsePackets(filename):
    parsedPackets = []

    for index, data in enumerate(PcapReader(filename)):
        direction, rawData = sanitize(raw(data))

        if direction == "IN":
            parsedPackets.append(CardToHostPacket(index, rawData))
        elif direction == "OUT":
            parsedPackets.append(HostToCardPacket(index, rawData))
        # TODO: Account for ATR

    return parsedPackets
