import opencage
from opencage.geocoder import OpenCageGeocode

import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier

import folium

number = "+905367930782"

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber, "en")
service_pro = phonenumbers.parse(number)
service = carrier.name_for_number(service_pro, "en")

print(pepnumber, location, service)

key = "d12ce5705c214513b2273cafa356d1bd"

geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)

lat = results[0]['geometry']['lat']
lng = results[0]['geometry']['lng']

print(lat, lng)

myMap = folium.Map(location=[lat, lng], zoom_start=9)
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("location.html")