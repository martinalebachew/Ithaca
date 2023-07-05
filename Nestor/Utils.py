# Utils.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

import binascii

HEX_DELIMITER = ":"


def hexify(data) -> str:
    if data != "":
        data = data.hex()

        if len(data) > 2:
            original = data
            data = HEX_DELIMITER.join(str(original[i:i+2]) for i in range(0, len(original), 2))

    return data
