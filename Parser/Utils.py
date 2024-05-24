# Utils.py
# (C) Martin Alebachew, 2023

from re import search
from typing import Tuple
from itertools import zip_longest
from Datagrams import Command, Response
from Shared import CardMetadata, Calypso, Preferences


def grouper(iterable, n, *, incomplete="fill", fillvalue=None):
    "Collect data into non-overlapping fixed-length chunks or blocks."
    # grouper("ABCDEFG", 3, fillvalue="x") → ABC DEF Gxx
    # grouper("ABCDEFG", 3, incomplete="strict") → ABC DEF ValueError
    # grouper("ABCDEFG", 3, incomplete="ignore") → ABC DEF
    iterators = [iter(iterable)] * n
    match incomplete:
        case "fill":
            return zip_longest(*iterators, fillvalue=fillvalue)
        case "strict":
            return zip(*iterators, strict=True)
        case "ignore":
            return zip(*iterators)
        case _:
            raise ValueError("Expected fill, strict, or ignore")


def hexify(data: bytes | int | None) -> str:
    if (data is None) or (data == b""):
        return ""
    
    if isinstance(data, int):
        data = data.to_bytes(1, "little")
    else:
        is_data_compressable = all((byte == data[0] for byte in data))
        is_data_compact = (len(data) <= max(Preferences.COMPACT_HEX_MAX_LENGTH, 1))
        if is_data_compressable and not is_data_compact:
            return f"[{hexify(data[0])}] * {len(data)}"
    
    # TODO: Replace with lighter logic
    data = grouper(data.hex(), 2, incomplete="strict")
    data = [''.join(number_digits) for number_digits in data]
    data = Preferences.HEX_DELIMITER.join(data)
    return data


def generalize_response_code(code: str) -> str | None:
    if len(code) != 4:
        raise ValueError("Unknown response code format!")

    if (code[2:4] == "——") or (code[1:4] == "XXX"):
        return None

    code = code.replace("X", "")[:-1]
    code += "X" * (4 - len(code))
    return code


def lookup_response_code(sw1: int, sw2: int) -> str | None:
    sw1 = hexify(sw1)
    sw2 = hexify(sw2)
    code = (sw1 + sw2 if sw2 else sw1 + "——").upper()

    while code is not None:
        if code in Calypso.RESPONSE_CODES:
            return Calypso.RESPONSE_CODES[code]
        code = generalize_response_code(code)

    return None


def lookup_chip_type(chip: int) -> str:
    chip = hexify(chip)
    if chip in CardMetadata.CHIP_TYPE:
        return CardMetadata.CHIP_TYPE[chip]
    
    return "N/A"


def lookup_standard(standard: int) -> str:
    standard = hexify(standard)
    if standard in CardMetadata.APPLICATION:
        return CardMetadata.APPLICATION[standard]
    
    return "N/A"


def lookup_issuer(issuer: int) -> str:
    issuer = hexify(issuer)
    if issuer in CardMetadata.SOFTWARE_ISSUER:
        return CardMetadata.SOFTWARE_ISSUER[issuer]
    
    return "N/A"


def get_command_notes(datagram: Command) -> Tuple[bool, str]:
    if hexify(datagram.ins) in Calypso.INSTRUCTION_CODES:
        instruction_text = Calypso.INSTRUCTION_CODES[hexify(datagram.ins)]
        instruction_source = "PROPRIETARY" if datagram.cla != b'\x00' else "ISO/IEC 7816"
        text = f"{instruction_text} ({instruction_source})"
        return (True, text)

    return (False, "Failed to analyse proprietary instruction!")


def get_response_notes(datagram: Response) -> Tuple[str, str]:
    response_text = lookup_response_code(datagram.sw1, datagram.sw2)
    status = search(Calypso.RESPONSE_STATUS_REGEX, response_text)[0]
    
    if status is None:
        status = "Error"
    
    return (status, response_text)
