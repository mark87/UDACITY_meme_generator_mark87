# Meme Generator

This is a web application that generates random or custom memes. An image will be overlaid with a quote from an author. The quotes are obtained from various file types that are read by the application. The image chosen is also formatted to be a specific width (500 pixels). This application also accpets dynamic user input through a command-line tool and a web service (Flask).

## Getting Started:

### Prerequisites

Download and install the pdftotext command line tool from: https://www.xpdfreader.com/download.html

##### Python Libraries Needed
Created requirements.txt file by using the following command in the command line interface on Windows 10. This file contains all of the libraries I had to download for the program to function properly.

'''bash
py -m  pipreqs.pipreqs .
'''

### Application

The web application can be started by running the command:
```bash
python app.py
```

The local meme application can be started by running the command:
```bash
python meme.py
```

You can access the application at: http://localhost:5000 or http://127.0.0.1:5000

#### Submodules



## Built With

* [Flask](http://flask.pocoo.org/) - The python server micro framework

## Acknowledgments

* [Udacity](https://www.udacity.com/)
