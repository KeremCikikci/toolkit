import requests
from bs4 import BeautifulSoup
import json

cities = None

try:
    with open('save.json', "r", encoding="utf-8") as dosya:
        cities = json.load(dosya)['cities']
    
except FileNotFoundError:
    print("File not found")

def get_wheather(city):
    url = "https://www.google.com/search?q="+"weather"+city

    html = requests.get(url).content

    soup = BeautifulSoup(html, 'html.parser')
    temp = soup.find('div', attrs={'class': 'BNeawe iBp4i AP7Wnd'}).text
    str = soup.find('div', attrs={'class': 'BNeawe tAd8D AP7Wnd'}).text

    data = str.split('\n')
    time = data[0]
    sky = data[1]

    listdiv = soup.findAll('div', attrs={'class': 'BNeawe s3v9rd AP7Wnd'})
    strd = listdiv[5].text

    pos = strd.find('Wind')
    other_data = strd[pos:]

    print("City: ", city)
    print("Temperature is", temp)
    print("Time: ", time)
    print("Sky Description: ", sky)
    print(other_data)

def add_city(city):
    try:
        with open('save.json', "r", encoding="utf-8") as dosya:
            veri = json.load(dosya)
        
        cities_ = veri.get("cities", [])
        
        cities_.append(city)
        
        if city not in cities_:
            cities_.append(city)

            with open('save.json', "w", encoding="utf-8") as dosya:
                json.dump({"cities": cities_}, dosya, indent=4)
        
    except:
        print("eklenemedi")

add_city("Stuttgart")

for city in cities:
    get_wheather(city)
