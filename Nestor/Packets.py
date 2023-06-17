# Packets.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

import json
import logging

from scapy.all import *

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def SafeAccessAttr(dictionary, key, defaultValue="", nestingKey=">"):
    value = dictionary
    path = [key] if nestingKey is None else key.split(nestingKey)

    for levelKey in path:
        if levelKey in value:
            value = value[levelKey]
        else:
            return defaultValue
    return value


class HostToCardPacket:
    def __init__(self, index, cardLayer):
        self.no = str(index + 1)

        self.cla = SafeAccessAttr(cardLayer, "iso7816.apdu.cla")[2:]
        self.ins = SafeAccessAttr(cardLayer, "iso7816.apdu.ins")[2:]
        self.p1 = SafeAccessAttr(cardLayer, "Parameters>iso7816.apdu.p1")[2:]
        self.p2 = SafeAccessAttr(cardLayer, "Parameters>iso7816.apdu.p2")[2:]
        self.lc = SafeAccessAttr(cardLayer, "iso7816.apdu.lc")[2:]
        self.data = SafeAccessAttr(cardLayer, "iso7816.apdu.body")
        self.le = SafeAccessAttr(cardLayer, "iso7816.apdu.le")[2:]
        self.serialized = (
            self.no,
            "H>C",
            self.cla,
            self.ins,
            self.p1,
            self.p2,
            self.lc,
            self.data,
            self.le,
        )


class CardToHostPacket:
    def __init__(self, index, cardLayer):
        self.no = str(index + 1)
        self.data = SafeAccessAttr(cardLayer, "iso7816.apdu.body")
        self.sw1 = SafeAccessAttr(cardLayer, "iso7816.apdu.sw1")[2:]
        self.sw2 = SafeAccessAttr(cardLayer, "iso7816.apdu.sw2")[2:]
        self.serialized = (self.no, "C>H", self.data, self.sw1, self.sw2)


def parsePackets(filename):
    parsedPackets = []
    with open(filename) as file:
        for i, packetData in enumerate(json.load(file)):
            packetData = packetData["_source"]

            if "iso7816" not in packetData["layers"].keys():
                continue

            usbLayer = packetData["layers"]["usb"]
            cardLayer = packetData["layers"]["iso7816"]

            if usbLayer["usb.src"] == "host":
                parsedPackets.append(HostToCardPacket(i, cardLayer))
            elif "iso7816.atr" not in cardLayer:  # Skip ATR
                parsedPackets.append(CardToHostPacket(i, cardLayer))

    return parsedPackets
