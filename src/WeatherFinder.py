#Python Project 1: Find the weather of a city using Open-Meteo API

import requests

city = input("Enter the city: ")

geo = requests.get(
    "https://geocoding-api.open-meteo.com/v1/search",
    params={"name" : city}

).json()

lat = geo["results"][0]["latitude"]
lon = geo["results"][0]["longitude"]
name = geo["results"][0]["name"]

data = requests.get(
    "https://api.open-meteo.com/v1/forecast",
    params={
        "latitude": lat,
        "longitude": lon,
        "current_weather": True
    }
).json()

temp = data["current_weather"]["temperature"]
wind = data["current_weather"]["windspeed"]


print("\nCITY: " + name)
print("TEMPERATURE: " + str(temp))
print("WIND SPEED: " + str(wind))