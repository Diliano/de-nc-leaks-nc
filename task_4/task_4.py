import requests
import json

"""
Automation is great. Create a function called `scavenge_for_nc_data` that uses all of the functions you 
created in Tasks 1-3 to automate your hunt for data.
"""

def get_people():
    response = requests.get("https://nc-leaks.herokuapp.com/api/people")
    formatted_response = response.json()

    results = []

    for person in formatted_response["people"]:
        if person["job"]["workplace"] == "northcoders":
            results.append(person)
            
    with open("task_4/northcoders.json", "w") as f:
        json.dump(results, f, indent=4)


def get_interests():
    with open("task_4/northcoders.json") as f:
        data = json.load(f)

    results = []

    for person in data:
        username = person["username"]
        url = f"https://nc-leaks.herokuapp.com/api/people/{username}/interests"
        response = requests.get(url)
        formatted_response = response.json()
        results.append(formatted_response["person"])

    with open("task_4/interests.json", "w") as f:
        json.dump(results, f, indent=4)


def get_pets():
    with open("task_4/northcoders.json") as f:
        data = json.load(f)

    results = []

    for person in data:
        username = person["username"]
        url = f"https://nc-leaks.herokuapp.com/api/people/{username}/pets"
        response = requests.get(url)
        if response.status_code == 200:
            results.append(response.json()["person"])
    
    with open("task_4/pets.json", "w") as f:
        json.dump(results, f, indent=4)


def scavenge_for_nc_data():
    get_people()
    get_interests()
    get_pets()

# scavenge_for_nc_data()