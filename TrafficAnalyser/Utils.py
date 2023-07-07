# Utils.py
# (C) Martin Alebachew, 2023

from Shared import RESPONSES
import binascii

HEX_DELIMITER = ":"


def hexify(data) -> str:
    if data != "":
        data = data.hex()

        if len(data) > 2:
            original = data
            data = HEX_DELIMITER.join(str(original[i:i+2]) for i in range(0, len(original), 2))

    return data


def generalize(code):
    if code is None or len(code) != 4:
        return None

    if code[2:4] == "——":
        return None

    if code[1:4] == "XXX":
        return None

    code = code.replace("X", "")
    code = code[:-1]
    code += "X" * (4 - len(code))
    return code


def lookupResponse(sw1, sw2):
    sw1 = hexify(sw1)
    sw2 = hexify(sw2)
    code = (sw1 + sw2 if sw2 else sw1 + "——").upper()

    # Generalize code until found in responses
    while code is not None:
        if code in RESPONSES.keys():
            return RESPONSES[code]
        code = generalize(code)

    return None
