# Shared.py
# (C) Martin Alebachew, 2023

VERSION = "0.1"
TABLE_WIDTH = 190

HEADERS = {
    "CardToHost": {
        "titles": ["NO", "DIR", "Data", "SW1", "SW2"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 143, 10, 10)]
    },

    "HostToCard": {
        "titles": ["NO", "DIR", "CLA", "INS", "P1", "P2", "Lc", "Data", "Le"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 10, 10, 10, 10, 10, 103, 10)]
    }
}

INSTRUCTIONS = {
    "04": "DEACTIVATE FILE",
    "0e": "ERASE BINARY",
    "10": "FABRICATION READ",
    "20": "VERIFY PIN",
    "30": "DECREASE",
    "32": "INCREASE",
    "38": "DECREASE MULTIPLE",
    "3a": "INCREASE MULTIPLE",
    "44": "ACTIVATE FILE / REHABILITATE",
    "52": "CHANGE SPEED",
    "7c": "SV GET",
    "82": "EXTERNAL AUTHENTICATE / MANAGE SECURE SESSION",
    "84": "GET CHALLENGE",
    "86": "GENERAL AUTHENTICATE / GIVE RANDOM",
    "8a": "OPEN SECURE SESSION",
    "8c": "ABORT SECURE SESSION",
    "8e": "CLOSE SECURE SESSION",
    "a2": "SEARCH RECORD",
    "a4": "SELECT FILE / SELECT APPLICATION",
    "b0": "READ BINARY",
    "b2": "SEARCH RECORD(S)",
    "b3": "READ RECORDS MULTIPLE",
    "b6": "READ RECORD STAMPED",
    "b8": "SV RELOAD",
    "ba": "SV DEBIT",
    "bc": "SV UNDEBIT",
    "be": "GET ATR",
    "c0": "GET RESPONSE",
    "ca": "RETRIEVE DATA",
    "d0": "WRITE BINARY",
    "d2": "WRITE RECORD",
    "d6": "UPDATE BINARY",
    "d8": "CHANGE KEY / CHANGE PIN",
    "da": "SET DATA",
    "dc": "UPDATE RECORD",
    "e0": "CREATE FILE",
    "e1": "GET AVAILABLE MEMORY",
    "e2": "APPEND RECORD",
    "f2": "STATUS",
}