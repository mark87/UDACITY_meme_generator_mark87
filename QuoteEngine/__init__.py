'''Base module for quote engine.
This extracts quotes from different file formats.
'''

from .Ingester import Ingester
from .QuoteModel import QuoteModel

from .DocxIngester import DocxIngester
from .CSVIngester import CSVIngester
from .TextIngester import TextIngester
from .PDFIngester import PDFIngester

