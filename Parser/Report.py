# Report.py
# (C) Martin Alebachew, 2023

from fpdf import FPDF
from Shared import VERSION, INSTRUCTIONS
from Packets import HostToCardPacket, CardToHostPacket
from Utils import hexify, lookupResponse
from ATR import ATRInformation


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

RESPONSE_COLOR = {
    "Unknown": "BLACK",
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


class Report:
    def __init__(self, date, title, author):
        self.__posY = 0  # Stores the current y pos in document

        # Create a document
        self.__pdf = FPDF()
        self.__pdf.add_page()
        self.__resetFont()
        self.__addInfo(date, title, author)

    def __resetFont(self):
        self.__pdf.set_font("Courier", size=10)
        self.__setFontBlack()

    def __setFontBold(self):
        self.__pdf.set_font("Courier", "B", size=10)

    def __setFontColor(self, colorName):
        self.__pdf.set_text_color(*COLOR_SCHEME[colorName])

    def __setResponseColor(self, status):
        self.__setFontColor(RESPONSE_COLOR[status].upper())

    def __setFontRed(self):
        self.__pdf.set_text_color(*COLOR_SCHEME["RED"])

    def __setFontGreen(self):
        self.__pdf.set_text_color(*COLOR_SCHEME["GREEN"])

    def __setFontBlack(self):
        self.__pdf.set_text_color(0, 0, 0)

    def __addText(self, text, upperPadding=0, fontSize=None):
        if fontSize is not None:
            oldSize = self.__pdf.font_size_pt
            self.__pdf.set_font_size(fontSize)
            self.__addTextImpl(upperPadding, text)
            self.__pdf.set_font_size(oldSize)
        else:
            self.__addTextImpl(upperPadding, text)

    def __addTextImpl(self, upperPadding, text):
        self.__pdf.cell(0, self.__pdf.font_size + upperPadding, txt=text, ln=1)
        # Adding a new cell with the given text, the width is set to 0, meaning that the cell can
        # expand until the right margin. ln is set to 1, which means that the document position pointer
        # will be updated to the next line. The cell height is set to the font size, plus padding after the text.

    def __addInfo(self, date, title, author):
        self.__addText('RavKav Traffic Analysis Report', fontSize=14)
        self.__addText(f'{title}, recorded by {author} on {date}\n')
        self.__addText(f'Ithaca Traffic Analyser {VERSION}')
        self.__pdf.y += 5  # Add break

    def addATRScan(self, ATRPacket):
        if not isinstance(ATRPacket, CardToHostPacket):
            raise "Invalid ATR packet!"

        if len(ATRPacket.data) != 17:
            raise "Invalid ATR data size!"

        ATRInfo = ATRInformation(ATRPacket)

        self.__addText("Extracted Answer-To-Reset Information", fontSize=12)

        self.__addText(f"Raw ATR: {ATRInfo.rawATR}")
        self.__addText(f"Chip: {ATRInfo.chip}")
        self.__addText(f"Standard (Application): {ATRInfo.standard}")
        self.__addText(f"File Structure: {ATRInfo.file_structure}")
        self.__addText(f"Software Issuer: {ATRInfo.software_issuer}")
        self.__addText(f"Software Version: {ATRInfo.software_version}")
        self.__addText(f"Serial Number (Lower DWORD): {ATRInfo.lower_serial}")

        self.__pdf.y += 5  # Add break

    def addRecords(self, parsedPacketsList):
        for parsedPacket in parsedPacketsList:
            self.addRecord(parsedPacket)

    def addRecord(self, parsedPacket):
        if isinstance(parsedPacket, HostToCardPacket):
            self.__addRecordImpl("HostToCard", parsedPacket)
        elif isinstance(parsedPacket, CardToHostPacket):
            self.__addRecordImpl("CardToHost", parsedPacket)
        else:
            raise TypeError("Parsed packet type is unknown!")

    def __addRecordImpl(self, direction, packet):
        with self.__pdf.table(
            first_row_as_headings=True,
            width=TABLE_WIDTH,
            col_widths=HEADERS[direction]["widths"]
        ) as table:
            table.row(HEADERS[direction]["titles"])  # Header row
            table.row([packet.serialized[i] for i in range(0, len(HEADERS[direction]["titles"]))])  # Data row

        # Notes row
        with self.__pdf.table(
                first_row_as_headings=False,
                width=TABLE_WIDTH
        ) as table:
            if direction == "HostToCard":
                if hexify(packet.ins) in INSTRUCTIONS.keys():
                    table.row([INSTRUCTIONS[hexify(packet.ins)] + (" (PROPRIETARY)" if packet.cla != b'\x00' else " (ISO/IEC 7816)")])
                else:
                    self.__setFontRed()
                    self.__setFontBold()
                    table.row(["Failed to analyse proprietary instruction!"])
                    self.__resetFont()
                    
            elif direction == "CardToHost":
                response = lookupResponse(packet.sw1, packet.sw2)
                status = response[response.find("[") + 1:response.find("]")] if response else "Error"
                response = response if response else "Failed to analyse card response!"

                self.__setResponseColor(status)
                self.__setFontBold()
                table.row([response])
                self.__resetFont()

    def save(self, filepath):
        self.__pdf.output(filepath)


if __name__ == "__main__":
    print(f"Percentage sum of C>H table widths: {sum(HEADERS['CardToHost']['widths'])}%")
    print(f"Percentage sum of H>C table widths: {sum(HEADERS['HostToCard']['widths'])}%")
    print(f"Values other than 100.0% might cause unexpected behavior.")
