# Shared.py
# (C) Martin Alebachew, 2023
# Nestor — RavKav Traffic Analysis Reports [ PROJECT ITHACA ]

VERSION = "0.1"
TABLE_WIDTH = 190

HEADERS = {
    "in": {
        "titles": ["NO", "DIR", "Data", "SW1", "SW2"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 143, 10, 10)]
    },

    "out": {
        "titles": ["NO", "DIR", "CLA", "INS", "P1", "P2", "Lc", "Data", "Le"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 10, 10, 10, 10, 10, 103, 10)]
    }
}

DIRCONV = {
    ">": "in",
    "<": "out"
}
