import requests
import json

"""
Write a function called `get_people` that will retrieve list of all the available people on the `northcoders` server . This should:

1. Use the [`requests`](https://pypi.org/project/requests/) module to make a request to `https://nc-leaks.herokuapp.com/api/people`.
2. Once you have the response body as a useable dictionary, look through the people to find anyone who has `northcoders` as the workplace.
3. Save these `northcoders` employees to a file called `northcoders.json`.
"""

def get_people():
    response = requests.get("https://nc-leaks.herokuapp.com/api/people")
    formatted_response = response.json()

    results = []

    for person in formatted_response["people"]:
        if person["job"]["workplace"] == "northcoders":
            results.append(person)
            
    with open("northcoders.json", "w") as f:
        f.write(json.dumps(results, indent=4))

# get_people()