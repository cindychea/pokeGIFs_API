import json
import requests
import os
key = os.environ.get("GIPHY_KEY")


res = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
body = json.loads(res.content)
print(body['name'])
print(body['id'])
print(body['types'])
print('---')

url = "https://api.giphy.com/v1/gifs/search?api_key={}&q=pikachu&rating=g".format(key)
res1 = requests.get(url)
body1 = json.loads(res1.content)
giphy_url = body1['data'][0]['url']
print(giphy_url)