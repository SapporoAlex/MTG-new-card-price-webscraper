# Webscraper for Magic the Gathering Card Prices

![MTGyo](https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/Magic_the_gathering-card_back.jpg/220px-Magic_the_gathering-card_back.jpg)

## Description
I built a simple webscraper that can take the prices and some basic details of the latest new available cards from this website.
I did this for a friend who is always looking for the latest deals from his favourite card dealer. The script uses playwright to navigate to the correct page and beautifulsoup
to parse the HTML. It then uses pandas to create a CSV file as well as an Excel file for my friend to easily read.

## Installation
You will need to install the following packages

```bash
pip install bs4, playwright, pandas
```

Copy the file to a directory of your choice

Run the file

```bash
python Hareruya.py
```

## License
This project is licensed under the MIT License.

## Author
Alex McKinley
