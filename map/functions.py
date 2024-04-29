from geopy.distance import geodesic as GD
from geopy.geocoders import Nominatim

def distance_cities(city1, city2): # kus bakisi
    geolocator = Nominatim(user_agent="MyApp")

    location_city1 = geolocator.geocode(city1)
    location_city2 = geolocator.geocode(city2)

    lat_long_city1 = (location_city1.latitude ,location_city1.longitude)
    lat_long_city2 = (location_city2.latitude ,location_city2.longitude)

    distance = GD(lat_long_city1 , lat_long_city2).km

    return distance



