'''Create class that encapsulates helper classes.
It contains logic that will decide which ingester to use based on filte type
'''
from typing import List

from .IngesterInterface import IngesterInterface
from .QuoteModel import QuoteModel

from .DocxIngester import DocxIngester
from .CSVIngester import CSVIngester
from .TextIngester import TextIngester
from .PDFIngester import PDFIngester


class Ingester(IngesterInterface):
    '''List all avaiable helper classes to read various file types'''
    ingesters = [DocxIngester, CSVIngester, TextIngester, PDFIngester]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''Try to injest file with each injester avaiable'''
        for ingester in cls.ingesters:
            if ingester.can_ingest(path):
                return ingester.parse(path)
