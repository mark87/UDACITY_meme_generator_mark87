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

### Quote Engine

## Built With

* [Flask](http://flask.pocoo.org/) - The python server micro framework

## Acknowledgments

* [Udacity](https://www.udacity.com/)
