import requests
import json

"""
Write a function called `get_pets` that does the same as the Task 2 but for pets. 

The endpoint is `https://nc-leaks.herokuapp.com/api/people/:username/pets`;

> Note: Some of the users do not have pets and so the server will give a 404 response! 

These responses should not be included in the `pets.json`. 

Consider how to you will use the status code to inform when to include some pets.
"""

def get_pets():
    with open("task_1/northcoders.json") as f:
        data = json.load(f)

    results = []

    for person in data:
        username = person["username"]
        url = f"https://nc-leaks.herokuapp.com/api/people/{username}/pets"
        response = requests.get(url)
        if response.status_code == 200:
            results.append(response.json()["person"])
    
    with open("task_3/pets.json", "w") as f:
        json.dump(results, f, indent=4)

# get_pets()