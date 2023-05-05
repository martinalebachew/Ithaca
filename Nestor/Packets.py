# Packets.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

import json
from scapy.all import *

class HostToCardPacket:
    def __init__(self, no, dir, cla, ins, p1, p2, lc, data, le):
        self.no = no
        self.dir = dir
        self.cla = cla
        self.ins = ins
        self.p1 = p1
        self.p2 = p2
        self.lc = lc
        self.data = data
        self.le = le


class CardToHostPacket:
    def __init__(self, no, dir, data, sw1, sw2):
        self.no = no
        self.dir = dir
        self.data = data
        self.sw1 = sw1
        self.sw2 = sw2


def main():
    with open("/Users/martin/Desktop/Ithaca Captures/Ithaca_charging.json") as file:
        for packetData in json.load(file):
            packetData = packetData["_source"]

            if "iso7816" not in packetData["layers"].keys():
                continue

            usbLayer = packetData["layers"]["usb"]
            cardLayer = packetData["layers"]["iso7816"]

            if usbLayer["usb.src"] == "host":
                HostToCardPacket(cardLayer)
            else:
                CardToHostPacket(cardLayer)


if __name__ == '__main__':
    main()
