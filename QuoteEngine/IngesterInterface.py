'''Define abstract base class with two methods.
---------------------------------------------------------------
def can_ingest() - Check to see if this is a valid file type
def parse() - Read contents of file and save to list of quotes
'''


from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel


class IngesterInterface(ABC):
    '''Abstract base class for an ingestor.'''

    allowed_extensions = ['csv', 'docx', 'pdf', 'txt']

    @classmethod
    def can_ingest(cls, path: str):
        '''Determine if a file path is found in allowed_extensions'''
        ext = path.split('.')[-1]
        return ext in cls.allowed_extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        '''Read contents of file and save to list of quotes'''
        pass
