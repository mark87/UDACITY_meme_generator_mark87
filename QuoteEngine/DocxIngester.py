from typing import List
import docx

from .IngesterInterface import IngesterInterface
from .QuoteModel import QuoteModel


class DocxIngester(IngesterInterface):
    allowed_extensions = ['docx']  # Add 'docx' as valid file type

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('no docx file in directory')

        quotes = []  # Define empty list to store quotes
        doc = docx.Document(path)  # Read docx into doc object

        for para in doc.paragraphs:  # Cycle through each line in document
            if para.text != "":  # Check to see if line is an empty string
                parse = para.text.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)  # Add new_quote to list of quotes

        return quotes
