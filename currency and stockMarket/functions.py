import requests
from bs4 import BeautifulSoup
import yfinance as yf

def get_currency(in_currency, out_currency, amount=1):
    url = f'https://www.x-rates.com/calculator/?from={in_currency}&to={out_currency}&amount={amount}'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'html.parser')
    rate = soup.find('span', class_='ccOutputRslt').get_text()

    return rate

def get_stockMarket(stock):
    stock = yf.Ticker(stock)
    price = stock.info['ask'] # bid
    print(price)