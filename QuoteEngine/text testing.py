



#path = r"C:\Users\mk832b\OneDrive - AT&T Services, Inc\Desktop\Coding Exercises\Meme_Generator\_data\DogQuotes\DogQuotesPDF.pdf"
#quotes = []  # Define empty list to store quotes
#with open(path, encoding="utf-8-sig") as f:
#    '''Read all lines of file into list of strings'''
#    lines = f.readlines()
#    for line in iter(lines):
#        '''Seperate each line into new list with body and author'''
#        parse = line.split(' - ')
##        new_quote = QuoteModel(parse[0], parse[1])
#  #      quotes.append(new_quote)  # Add new_quote to list of quotes


path = r"C:\Users\mk832b\OneDrive - AT&T Services, Inc\Desktop\Coding Exercises\Meme_Generator\QuoteEngine\2313040.txt"
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
                new_quote = QuoteModel(parsed[0], parsed[1])
                quotes.append(new_quote)  # Add new_quote to list of quotes

