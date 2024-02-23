# ATR.py
# (C) Martin Alebachew, 2024

from Packets import CardToHostPacket
from Utils import hexify, lookupChipType, lookupStandard, lookupIssuer


class ATRInformation:
    def __init__(self, ATRPacket):
        if not isinstance(ATRPacket, CardToHostPacket):
            raise "Invalid ATR packet!"

        ATRData = ATRPacket.data
        historical_bytes = ATRData[4:]

        # Note: using single-byte arrays to disable int conversion
        
        self.rawATR = hexify(ATRData)
        
        self.chip = historical_bytes[2:3]
        self.chip = f"{lookupChipType(self.chip)} ({hexify(self.chip)})"
        
        self.standard = historical_bytes[3:4]
        self.standard = f"{lookupStandard(self.standard)} ({hexify(self.standard)})"
        
        self.file_structure = f"#{historical_bytes[4]}"
        
        self.software_issuer = historical_bytes[5:6]
        self.software_issuer = f"{lookupIssuer(self.software_issuer)} ({hexify(self.software_issuer)})"
        
        self.software_version = f"{hexify(historical_bytes[6:8])} (ROM, EEPROM)"
        
        self.lower_serial = historical_bytes[8:12]
        self.lower_serial = f"{int.from_bytes(self.lower_serial, byteorder='big')} ({hexify(self.lower_serial)})"
