from typing import List

from .IngesterInterface import IngesterInterface
from .QuoteModel import QuoteModel

import subprocess
import random
import os


class PDFIngester(IngesterInterface):
    allowed_extensions = ['pdf']  # Add 'pdf' as valid file type

    #path = r"C:\Users\mk832b\OneDrive - AT&T Services, Inc\Desktop\Coding Exercises\Meme_Generator\_data\DogQuotes\DogQuotesPDF.pdf"

    '''Convert PDF to txt file'''
    @staticmethod
    def pdftotext(path: str) -> str:
        pdf_txt_file = f'./{random.randint(0, 10000000)}.txt'

        try:
            call = subprocess.call(['pdftotext', path, pdf_txt_file])
            return pdf_txt_file
        except Exception:
            os.remove(pdf_txt_file)
            msg = ("File path incorrect or PDF to TXT conversion failed")
            raise OSError()

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        path = cls.pdftotext(path)
        quotes = []  # Define empty list to store quotes
        with open(path, 'r') as f:
            '''Read all lines of file into list of strings'''
            lines = f.readlines()
            for line in lines:
                '''Seperate each line into new list with body and author'''
                line = line.strip()
                if len(line) > 0:
                    parse = line.split(' "')
                    for section in parse:
                        parsed = section.split(' - ')
                        body = '"' + parsed[0]
                        author = parsed[1]
                        new_quote = QuoteModel(body, author)
                        quotes.append(new_quote)  # Add new_quote to list
        os.remove(path)
        return quotes
