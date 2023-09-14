import requests
from bs4 import BeautifulSoup as bs
import pandas as pd


URL_TEMPLATE = "https://www.avito.ru/tambov/noutbuki?cd=1&q=macbook+air+m1"
FILE_NAME = "test.csv"

def parse(url = URL_TEMPLATE):
    result_list = {'href': [], 'title': [], 'price': []}
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    macbook_names = soup.find_all('div', class_='iva-item-title-py3i_')
    macbook_price = soup.find_all('div', class_='price-price-JP7qe')
    for name in macbook_names:
        result_list['href'].append('https://www.avito.ru'+name.a['href'])
        result_list['title'].append(name.a['title'])
    for info in macbook_price:
        result_list['price'].append(info.text)
    return result_list

df = pd.DataFrame(data=parse())
df.to_csv(FILE_NAME)