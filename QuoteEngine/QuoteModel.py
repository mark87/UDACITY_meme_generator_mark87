'''Create class for quotes to encapsulate the body and author.

Attributes:
    body: str - the body text of the quote
    author: str - the author text of the quote
'''


class QuoteModel():
    '''Base class for a quote'''

    def __init__(self, body: str, author: str) -> None:
        '''Create quote object'''
        self.body = body
        self.author = author

    def __repr__(self):
        '''Return string representation of the quote'''
        return f'{self.body} - {self.author}'
