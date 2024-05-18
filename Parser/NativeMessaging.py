# NativeMessaging.py
# (C) Martin Alebachew, 2024

import sys
import struct

LENGTH_SIZE = 4


def disableOutputAltering() -> None:
  # TODO: Make sure Windows does not replace /n with /r/n
  pass


def encodeLength(data: bytes) -> bytes:
  return struct.pack('>I', len(data))


def out(data: bytes) -> None:
  disableOutputAltering()
  sys.stdout.buffer.write(encodeLength(data))
  sys.stdout.buffer.write(data)
