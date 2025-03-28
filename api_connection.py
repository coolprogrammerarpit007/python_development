# Connecting an API 

import requests

URL = "https://pokeapi.co/api/v2/"

# method to get the pokemon Info

def pokemon_info(pokemon_name):
    url = f"{URL}/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        print("Data Fetched Sucessfully!")
        data = response.json()
        return data
    else:
        print("Failed to Fetch Data",response.status_code)

pokemon_name = input("Enter Pokemon Name: ")
pokemon_stats = pokemon_info(pokemon_name)
# print(pokemon_stats)

if pokemon_stats:
    print(f"{pokemon_name} : {pokemon_stats["id"]}")
else:
    print("pokemon not found!")