import requests
import json

response = requests.get("https://catfact.ninja/fact")
data = response.json()
print(data)

data = json.dumps(data, indent=4)
print(data)