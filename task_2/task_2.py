import requests
import json
from pprint import pprint

"""
Write a function called `get_interests` that uses the newly found usernames for each northcoder to retrieve information on everyone's interests. This function should:

1. Read the `northcoders.json` file you created in task 1
2. For every person, use their `username` and make a request to `https://nc-leaks.herokuapp.com/api/people/:username/interests` to get their interests.
3. Each response will be a JSON with a person key. Collect up the data on this `person` key into a list.
4. Once you have all responses in the list, save it to a file called `interests.json`.
"""

def get_interests():
    with open("task_1/northcoders.json") as f:
        data = json.load(f)

    results = []

    for person in data:
        username = person["username"]
        url = f"https://nc-leaks.herokuapp.com/api/people/{username}/interests"
        response = requests.get(url)
        formatted_response = response.json()
        results.append(formatted_response["person"])

    with open("task_2/interests.json", "w") as f:
        json.dump(results, f, indent=4)

# get_interests()