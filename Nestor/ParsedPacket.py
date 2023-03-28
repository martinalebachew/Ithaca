# ParsedPacket.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

class ParsedPacket:
    def __init__(self, dir):
        self.dir = dir
        self.data = ("34", "->", "0x34AB48", "0x2", "0x7")
