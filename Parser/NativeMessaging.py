# NativeMessaging.py
# (C) Martin Alebachew, 2024

import sys
import struct

LENGTH_SIZE = 4


def encode_length(data: bytes) -> bytes:
    return struct.pack('>I', len(data))


def out(data: bytes) -> None:
    # Note: using print will make alterations to the
    # output, for example replacing /n with /r/n on
    # Windows systems.
    sys.stdout.buffer.write(encode_length(data))
    sys.stdout.buffer.write(data)
