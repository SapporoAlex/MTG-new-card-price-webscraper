# Webscraper for Magic the Gathering Card Prices

!MTGyo[https://www.google.com/url?sa=i&url=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FMagic%3A_The_Gathering&psig=AOvVaw0W4_ehH7Jyd84YKVjbmEq2&ust=1703610737261000&source=images&cd=vfe&opi=89978449&ved=0CBIQjRxqFwoTCLC479mKq4MDFQAAAAAdAAAAABAE]

## Description
I built a simple webscraper that can take the prices and some basic details of the latest new available cards from this website.
I did this for a friend who is always looking for the latest deals from his favourite card dealer. The script uses playwright to navigate to the correct page and beautifulsoup
to parse the HTML. It then uses pandas to create a CSV file as well as an Excel file for my friend to easily read.

## Installation
You will need to intall the following packages

```bash
python pip install bs4, playwright, pandas
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
