# ReportConfig.py
# (C) Martin Alebachew, 2024

 
FONT = "Courier"
SIZE = 10
TITLE_SIZE = 14
HEADING_SIZE = 12

TABLE_WIDTH = 190

HEADERS = {
    "Response": {
        "titles": ["NO", "DIR", "Data", "SW1", "SW2"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 143, 10, 10)]
    },

    "Command": {
        "titles": ["NO", "DIR", "CLA", "INS", "P1", "P2", "Lc", "Data", "Le"],
        "widths": [(size * 100 / TABLE_WIDTH) for size in (15, 12, 10, 10, 10, 10, 10, 103, 10)]
    }
}

RESPONSE_COLOR = {
    "Unknown": "YELLOW",
    "Success": "GREEN",
    "Info": "BLACK",
    "Warning": "YELLOW",
    "Error": "RED",
}

COLOR_SCHEME = {
    "BLACK": (0, 0, 0),
    "GREEN": (93, 187, 99),
    "RED": (220, 40, 40),
    "YELLOW": (255, 191, 0)
}
