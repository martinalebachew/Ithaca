# Packets.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

import json
from scapy.all import *

class OutPacket:
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


class InPacket:
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

            if "iso7816" in packetData["layers"].keys():
                cardLayer = packetData["layers"]["iso7816"]
                print(cardLayer)


if __name__ == '__main__':
    main()
