# Meme Generator

This is a web application that generates random or custom memes. An image will be overlaid with a quote from an author. The quotes are obtained from various file types that are read by the application. The image chosen is also formatted to be a specific width (500 pixels). This application also accpets dynamic user input through a command-line tool and a web service (Flask).

## Getting Started:

### Prerequisites

Download and install the pdftotext command line tool from: https://www.xpdfreader.com/download.html

##### Python Libraries Needed
Created "requirements.txt" file by using the following command in the command line interface on Windows 10. This file contains all of the libraries I had to download for the program to function properly.

```bash
py -m  pipreqs.pipreqs .
```

### How to Run Application

To run the local meme generator use the command line interface and type in the following below. The '--arg {arg_tring}' are optional arguments.

```bash
py meme.py --path {image_path} --body {quote_body} -- author {quote_author}
```

To run the web app use the command line interface and type in the following below.
```bash
py app.py
```

You can access the web application at: http://localhost:5000 or http://127.0.0.1:5000

## Module Descriptions
This project has two engines. A QuoteEngine and a MemeEngine. They both help create memes from images and text found in various file types.

### QuoteEngine
The QuoteEngine module reads quotes from various file types (txt, docx, pdf, csv) and saves it into a quote list. This engine is capable of reading in new file types as long as the a new module file is created for the new file type. This is because some file types require special python libraries in order to be read correctly. This new file is consider an "Injester".

### MemeEngine
The MemeEngine module has an image manipulator class MemeEngine the can modify an image and save it to a path. This image is modified based on class attribute parameters.

```bash
'''Define meme format attributes'''
    meme_fill = 'white'  # Text fill color
    meme_factor = 18  # Font scale smalller relative to width
    meme_font = './arial.ttf'  # truetype font of the meme
    ```

## Built With

* [Flask](http://flask.pocoo.org/) - The python server micro framework

## Acknowledgments

* [Udacity](https://www.udacity.com/)
