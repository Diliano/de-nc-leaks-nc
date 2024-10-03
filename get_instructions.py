import requests
import json

response = requests.get("https://nc-leaks.herokuapp.com/api/top-secret")

formatted_response = response.json()
instructions = formatted_response["instructions"]

with open("instructions.md", "w") as f:
    f.write(instructions)