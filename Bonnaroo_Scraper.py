import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep

HEADERS = ({'User-Agent':
                'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0',
            'Accept-Language': 'en-US, en;q=0.5'})

exchange_data = pd.read_csv('ExchangeData.csv', sep=';')
exchange_data_urls = exchange_data.url

exchange_page = requests.get(exchange_data_urls[0], headers=HEADERS)

### try using requests-html or Selenium to exec JavaScript before souping in

soup = BeautifulSoup(exchange_page.content, features="lxml")

# price = soup.select('button[data-inventory-type=\'16\'] > span > span:nth-child(2)')

print(soup)
