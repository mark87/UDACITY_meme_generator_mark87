from typing import List

from .IngesterInterface import IngesterInterface
from .QuoteModel import QuoteModel


class TextIngester(IngesterInterface):
    allowed_extensions = ['txt']  # Add 'txt' as valid file type

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('no txt file in directory')

        quotes = []  # Define empty list to store quotes

        with open(path, encoding='utf-8-sig') as f:
            '''Read all lines of file into list of strings'''
            lines = f.readlines()
            for line in lines:
                '''Seperate each line into new list with body and author'''
                parse = line.split(' - ')
                new_quote = QuoteModel(parse[0], parse[1])
                quotes.append(new_quote)  # Add new_quote to list of quotes

        return quotes
