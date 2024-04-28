import requests
from bs4 import BeautifulSoup

page = requests.get('https://www.x-rates.com/calculator/?from=GBP&to=USD&amount=1')
soup = BeautifulSoup(page.text, 'html.parser')
price_box = soup.find(class_="ccOutputRslt")
rate = price_box
print(rate) #checking the output

def gbp_to_usd(rate,gbp):
    dollars=gbp*rate
    return dollars
gbp = input("Enter GBP amount: ")
finalamt = gbp_to_usd(float(rate),float(gbp))
print(str(gbp)+" GBP is equvalent to "+"$"+str(finalamt)+" USD")