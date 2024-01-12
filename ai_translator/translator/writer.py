import os
from reportlab.lib import colors,pagesizes,units
from reportlab.lib.styles import getSampleStyleSheet,ParagraphStyle
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    SimpleDocTemplate,Paragraph,Spacer,Table,TableStyle,PageBreak
)

from book import Book,ContentType
from utils import LOG

class Writer:
    def __init__(self):
        pass

    def save_translated_book(self,book:Book,output_file_path:str = None,file_format:str="PDF"):
        if file_format.lower() == "pdf":
            self._save_translated_book_pdf(book,output_file_path)
        elif file_format.lower() == "markdown":
            self._save_translated_book_markdown(book,output_file_path)
        else:
            raise ValueError(f"Unsupport file format:{file_format}")


    def _save_translated_book_pdf(self,book:Book,output_file_path:str=None):
        if output_file_path is None:
            output_file_path=book.pdf_file_path.replace('.pdf',f'_translated.pdf')

        LOG.info(f"pdf_file_path:{book.pdf_file_path}")
        LOG.info(f"开始翻译:{output_file_path}")
        
            