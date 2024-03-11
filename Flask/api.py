import requests
import json

response = requests.get("https://catfact.ninja/fact")
data = response.json()
print(data)


value = response.text
#value = json.loads(value)
print(value)

# info = value['fact']
# print(info)
