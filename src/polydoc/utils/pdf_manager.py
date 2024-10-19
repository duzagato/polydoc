import fitz

class PdfManager:
    def __init__(self, pdf_path: str) -> None:
        self.__doc = fitz.open(pdf_path)

    def get_table_of_contents(self) -> list:
        toc = self.__doc.get_toc()

        return toc