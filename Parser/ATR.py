# ATR.py
# (C) Martin Alebachew, 2024

from Datagrams import Response
from Utils import hexify, lookup_chip_type, lookup_standard, lookup_issuer


class ATRInformation:
    def __init__(self, atr_packet: Response):
        if not isinstance(atr_packet, Response):
            raise TypeError("Invalid ATR packet!")
        
        atr_data = atr_packet.data
        if len(atr_data) != 17:
            raise ValueError("Invalid ATR data size!")

        historical_bytes = atr_data[4:]
        
        self.raw_atr = hexify(atr_data)
        
        raw_chip = historical_bytes[2]
        self.chip = f"{lookup_chip_type(raw_chip)} ({hexify(raw_chip)})"
        
        raw_standard = historical_bytes[3]
        self.standard = f"{lookup_standard(raw_standard)} ({hexify(raw_standard)})"
        
        self.file_structure = f"#{historical_bytes[4]}"
        
        raw_issuer = historical_bytes[5]
        self.software_issuer = f"{lookup_issuer(raw_issuer)} ({hexify(raw_issuer)})"
        
        self.software_version = f"{hexify(historical_bytes[6:8])} (ROM, EEPROM)"
        
        raw_serial = historical_bytes[8:12]
        parsed_serial = int.from_bytes(raw_serial, byteorder='big')
        self.lower_serial = f"{parsed_serial} ({hexify(raw_serial)})"
