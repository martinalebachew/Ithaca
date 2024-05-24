# Report.py
# (C) Martin Alebachew, 2023

from fpdf import FPDF
from typing import List, Tuple
from ATR import ATRInformation
from Datagrams import Command, Response
from Shared import Preferences, ReportConfig
from Utils import hexify, get_command_notes, get_response_notes


class Report:
    def __init__(self, title: str):
        self.__posY = 0

        self.__pdf = FPDF()
        self.__pdf.add_page()
        self.__reset_font()
        self.__add_info(title)


    def __reset_font(self) -> None:
        self.__pdf.set_font(ReportConfig.FONT, size=ReportConfig.SIZE)
        self.__set_font_black()


    def __set_font_bold(self) -> None:
        self.__pdf.set_font(ReportConfig.FONT, "B", size=ReportConfig.SIZE)


    def __set_font_color(self, color_name: str) -> None:
        self.__pdf.set_text_color(*ReportConfig.COLOR_SCHEME[color_name])


    def __set_font_black(self) -> None:
        self.__set_font_color("BLACK")


    def __add_text(self, text: str, upper_padding: int = 0, font_size: int = None) -> None:
        if font_size is not None:
            old_size = self.__pdf.font_size_pt
            self.__pdf.set_font_size(font_size)
            self.__add_text_impl(upper_padding, text)
            self.__pdf.set_font_size(old_size)
        else:
            self.__add_text_impl(upper_padding, text)


    def __add_text_impl(self, upper_padding: int, text: str) -> None:
        self.__pdf.cell(0, self.__pdf.font_size + upper_padding, txt=text, ln=1)
        # Adds a new cell with the given text, the width is set to 0, meaning that the cell can
        # expand until the right margin. ln is set to 1, which means that the document position pointer
        # will be updated to the next line. The cell height is set to the font size, plus padding after the text.


    def __add_info(self, title: str) -> None:
        self.__add_text('RavKav Traffic Analysis Report', font_size=ReportConfig.TITLE_SIZE)
        self.__add_text(f'{title}\n')
        self.__add_text(f'Ithaca Parser {Preferences.VERSION}')
        self.__pdf.y += 5  # Add break


    def add_atr_scan(self, atr_packet: Response) -> None:
        atr_info = ATRInformation(atr_packet)

        # TODO: Move into ATRInformation class
        self.__add_text("Extracted Answer-To-Reset Information", font_size=ReportConfig.HEADING_SIZE)
        self.__add_text(f"Raw ATR: {atr_info.raw_atr}")
        self.__add_text(f"Chip: {atr_info.chip}")
        self.__add_text(f"Standard (Application): {atr_info.standard}")
        self.__add_text(f"File Structure: {atr_info.file_structure}")
        self.__add_text(f"Software Issuer: {atr_info.software_issuer}")
        self.__add_text(f"Software Version: {atr_info.software_version}")
        self.__add_text(f"Serial Number (Lower DWORD): {atr_info.lower_serial}")

        self.__pdf.y += 5  # Add break


    def add_records(self, datagrams: List[Command | Response]) -> None:
        for datagram in datagrams:
            self.add_record(datagram)


    def add_record(self, datagram: Command | Response) -> None:
        if isinstance(datagram, Command):
            self.__add_record_impl("Command", datagram)
        elif isinstance(datagram, Response):
            self.__add_record_impl("Response", datagram)
        else:
            raise TypeError("Unknown datagram type!")


    def __add_record_impl(self, datagram_type: str, datagram: Command | Response) -> None:
        self.__add_data_rows(datagram_type, datagram)
        self.__add_notes_row(datagram_type, datagram)
        
        
    def __format_data_row(self, datagram_type: str, datagram: Command | Response) -> List[str]:
        if datagram_type == "Command":
            data_row = [str(datagram.index + 1), "H>C", datagram.cla, datagram.ins, datagram.p1, datagram.p2, datagram.lc, datagram.data, datagram.le]
        elif datagram_type == "Response":
            data_row = [str(datagram.index + 1), "C>H", datagram.data, datagram.sw1, datagram.sw2]
        else:
            raise TypeError("Unknown datagram type!")
        
        for i in range(2, len(data_row)):
            data_row[i] = hexify(data_row[i])

        return data_row


    def __format_notes_row(self, datagram_type: str, datagram: Command | Response) -> Tuple[List[str], str]:
        if datagram_type == "Command":
            (found, text) = get_command_notes(datagram)
            return ([text], "BLACK" if found else "RED")
        
        if datagram_type == "Response":
            (status, text) = get_response_notes(datagram)
            return ([text], ReportConfig.RESPONSE_COLOR[status])
            
        raise TypeError("Unknown datagram type!")


    def __add_data_rows(self, datagram_type: str, datagram: Command | Response) -> None:
        row = self.__format_data_row(datagram_type, datagram)
        
        with self.__pdf.table(
            first_row_as_headings=True,
            width=ReportConfig.TABLE_WIDTH,
            col_widths=ReportConfig.HEADERS[datagram_type]["widths"]
        ) as table:
            table.row(ReportConfig.HEADERS[datagram_type]["titles"])
            table.row(row)


    def __add_notes_row(self, datagram_type: str, datagram: Command | Response) -> None:
        (row, color) = self.__format_notes_row(datagram_type, datagram)
        
        with self.__pdf.table(
            first_row_as_headings=False,
            width=ReportConfig.TABLE_WIDTH
        ) as table:
            self.__set_font_color(color)
            self.__set_font_bold()
            table.row(row)
            self.__reset_font()


    def save(self, filepath: str) -> None:
        self.__pdf.output(filepath)
