from fpdf import FPDF
from NestorConsts import VERSION


class Report:
    def __init__(self, date, title, author):
        self.__posY = 0  # Stores the current y pos in document

        # Create a document
        self.__pdf = FPDF()
        self.__pdf.add_page()
        self.__pdf.set_font("Courier", size=14)
        self.__addInfo(date, title, author)

    def __addText(self, text, upperPadding=0, fontSize=None):
        if fontSize is not None:
            oldSize = self.__pdf.font_size_pt
            self.__pdf.set_font_size(fontSize)
            self.__addTextInternal(upperPadding, text)
            self.__pdf.set_font_size(oldSize)
        else:
            self.__addTextInternal(upperPadding, text)

    def __addTextInternal(self, upperPadding, text):
        self.__pdf.cell(0, self.__pdf.font_size + upperPadding, txt=text, ln=1)
        # Adding a new cell with the given text, the width is set to 0, meaning that the cell can
        # expand until the right margin. ln is set to 1, which means that the document position pointer
        # will be updated to the next line. The cell height is set to the font size, plus padding after the text.

    def __addInfo(self, date, title, author):
        self.__addText('RavKav Traffic Analysis Report', fontSize=18)
        self.__addText(f'{title}, recorded by {author}\n')
        self.__addText(f'Generated by Nestor {VERSION} on {date}')
        self.__pdf.y += 10  # Add break

    def save(self, filepath):
        self.__pdf.output(filepath)
