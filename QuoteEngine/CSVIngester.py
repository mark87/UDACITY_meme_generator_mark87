'''Class will read CSV file types'''
from typing import List
import pandas

from .IngesterInterface import IngesterInterface
from .QuoteModel import QuoteModel


class CSVIngester(IngesterInterface):
    allowed_extensions = ['csv']  # Add 'csv' as valid file type

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('no csv file in directory')

        quotes = []  # Define empty list to store quotes
        df = pandas.read_csv(path, header=0)  # Read data into dataframe

        for index, row in df.iterrows():  # Cycle through each row in dataframe
            new_quote = QuoteModel(row['body'], row['author'])
            quotes.append(new_quote)  # Add new_quote to list of quotes

        return quotes
