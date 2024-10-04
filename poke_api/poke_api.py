import requests
import json
from time import sleep

"""
Well done for getting this far Detective! Now you've completed the core tasks, 
you should broaden the scope of this investigation by making requests to other servers.

You should firstly take some time to read the documentation for your chosen API and try out various requests to see what response data you can get. 
Then, create some functions similar to the ones in previous tasks, based around the ideas of:

- Requesting and storing data
- Filtering data according to some criteria
- Collating data from multiple requests
"""



"""
The PokeAPI defaults to 20 resources unless specified. 

The function below makes a request and tests the use of a query limit to override the default.

The name and url of each are extracted and written to the 'pokemon.json' file.
"""

def get_30_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/?limit=30")

    results = response.json()["results"]

    with open("poke_api/pokemon.json", "w") as f:
        json.dump(results, f, indent=4)

# get_30_pokemon()



"""
Each Pokemon has abilities.

The function below extracts the name and url of each Pokemon in 'pokemon.json' and then makes a request to the PokeAPI using the url.

The abilities are extracted from the request and formatted as a dictionary in the form {pokemon_name: list_of_abilities}

The formatted dictionaries are stored in a list and then written to the 'abilities.json' file
"""

def get_abilities():
    with open("poke_api/pokemon.json") as f:
        data = json.load(f)

    results = []

    for pokemon in data:
        name = pokemon["name"]
        url = pokemon["url"]
        response = requests.get(url)
        pokemon_data = response.json()
        ability_data = pokemon_data["abilities"]
        abilities = [ability["ability"]["name"] for ability in ability_data]
        results.append({name: abilities})

    with open("poke_api/abilities.json", "w") as f:
        json.dump(results, f, indent=4)

# get_abilities()



"""
A Pokemon may have an area or group of areas that they can be found in the wild.

The function below extracts the name and url of each Pokemon in 'pokemon.json' and then makes a request to the PokeAPI using the url.

The location areas are extracted from the request and formatted as a dictionary in the form {pokemon_name: location_areas}

The formatted dictionaries are stored in a list and then written to the 'locations.json' file
"""

def get_location_areas():
    with open("poke_api/pokemon.json") as f:
        data = json.load(f)

    results = []

    for pokemon in data:
        name = pokemon["name"]
        url = f"{pokemon['url']}encounters"
        response = requests.get(url)
        pokemon_data = response.json()
        locations = [location["location_area"]["name"] for location in pokemon_data]
        if not locations:
            locations = "You can't find this Pokemon in the wild"
        results.append({name: locations})

    with open("poke_api/locations.json", "w") as f:
        json.dump(results, f, indent=4)

# get_location_areas()


def get_pokemon_info():
    print("Preparing Pokemon...")
    sleep(2)
    get_30_pokemon()
    print("Your 30 Pokemon have been stored in the 'pokemon.json' file!")
    sleep(2)

    print("Sourcing Pokemon abilities...")
    sleep(2)
    get_abilities()
    print("The abilities of your Pokemon have been saved to the 'abilities.json' file!")
    sleep(2)

    print("Tracking down location details...")
    sleep(2)
    get_location_areas()
    print("The areas your Pokemon can be found in have been stored in the 'locations.json' file!")

# get_pokemon_info()