import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingester
from MemeEngine import MemeEngine

app = Flask(__name__)

meme = MemeEngine('./static')


def setup():
    """ Load all resources """

    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv']

    # Define list to hold all quotes
    quotes = []

    for file in quote_files:
        for quote in Ingester.parse(file):
            quotes.append(quote)

    images_path = "./_data/photos/dog/"
    # Define list to hold all image file names
    image_list = []

    # Look at each file in image_path directory
    for image in os.listdir(images_path):
        # Save file name to image_list list
        image_list.append(image)

    imgs = image_list

    return quotes, imgs


quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """
    tmp = "./temp_image.jpg"
    img_url = request.form.get["image_url"]
    img_data = requests.get(img_url, allow_redirects=True)
    try:
        with open(tmp, 'wb') as open_file:
            open_file.write(img_data.content)
            body = request.form["body"]
            author = request.form["author"]
            path = meme.make_meme(tmp, body, author)
            os.remove(tmp)
        return render_template('meme.html', path=path)
    except:
        return render_template('error.html')


if __name__ == "__main__":
    app.run()


