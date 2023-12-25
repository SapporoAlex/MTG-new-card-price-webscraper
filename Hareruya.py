from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import pandas as pd


with sync_playwright() as p:
    browser = p.chromium.launch(headless=True, slow_mo=50)
    page = browser.new_page()
    page.goto('https://www.hareruyamtg.com/en/')
    page.wait_for_selector('#newArrSp > div > ul')

    html = page.inner_html('#newArrSp')
    soup = BeautifulSoup(html, 'html.parser')
    new_arrivals_list_web = soup.text.strip()
    print(new_arrivals_list_web)
    name = []
    price = []
    stock = []
    for line in new_arrivals_list_web.splitlines():
        if len(line.lstrip()) > 20:
            name.append(line.strip())
        if '¥' in line:
            price.append(line)
        if 'Stock' in line:
            stock.append(line.strip())
    combined_list = list(zip(name, price, stock))

    # Convert the list of tuples into a dictionary
    result_dict = {'name': [item[0] for item in combined_list],
                   'price': [item[1] for item in combined_list],
                   'stock': [item[2] for item in combined_list]}

    df = pd.DataFrame(result_dict)
    df.to_excel('Hareruya New Arrivals.xlsx', index=False)

    browser.close()
