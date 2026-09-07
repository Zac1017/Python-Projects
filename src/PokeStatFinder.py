#Python Project 4: Find the stats of a Pokemon using PokeAPI

import requests

pokemon = input("\nEnter the name of the Pokemon you wish to find the stats for: ").lower()

response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

weight = response.json()["weight"]
height = response.json()["height"]
base_experience = response.json()["base_experience"]

abilities = [ability["ability"]["name"] for ability in response.json()["abilities"]]

print(f"\nPokemon: {pokemon.capitalize()}")
print(f"Weight: {weight}")
print(f"Height: {height}")
print(f"Base Experience: {base_experience}")
print(f"Abilities: {', '.join(abilities)}\n")

