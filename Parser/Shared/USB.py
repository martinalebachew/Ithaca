# USB.py
# (C) Martin Alebachew, 2024


# More information about URB:
# https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-usb.c
class URB:
    TRANSFER_TYPE_OFFSET = 22
    ENDPOINT_OFFSET = 21
    ENDPOINT_DIRECTION_MASK = 0x80
    DIRECTION_IN = ENDPOINT_DIRECTION_MASK
    DIRECTION_OUT = 0
    BULK = 0x03

# More information about USB CCID:
# https://github.com/boundary/wireshark/blob/master/epan/dissectors/packet-usb-ccid.c
class CCID:
    LAYER_LENGTH = 10
    MESSAGE_TYPE_OFFSET = 0
    PC_TO_READER_XFR = 0x6f
    READER_TO_PC_DATA = 0x80
