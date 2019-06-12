import requests
import json
import os
import random
from django.http import JsonResponse
key = os.environ.get("GIPHY_KEY")


def pokegif_show(request, id):
    res = requests.get(f"http://pokeapi.co/api/v2/pokemon/{id}/")
    if res.ok is False:
        return JsonResponse({'status': 'false', 'message': 'Sorry, that pokemon is invalid'}, status=404)
    
    body = json.loads(res.content)
    name = body["name"]
    id = body["id"]
    types = body["types"]


    res1 = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={key}&tag={name}&rating=g")
    if res1.ok is False:
        return JsonResponse({'status': 'false', 'message': 'Sorry, that api key is invalid'}, status=404)

    body1 = json.loads(res1.content)
    if len(body1['data']) < 1:
        return JsonResponse({'status': 'false', 'message': 'Sorry, there are no gifs!'}, status=404)
    
    giphy_url = body1['data']['url']

    return JsonResponse({
        "id": id,
        "name": name,
        "types": types,
        "gif": giphy_url
        })


def pokegif_team(request):
    res = requests.get("http://pokeapi.co/api/v2/pokemon-species/?limit=0")
    body = json.loads(res.content)
    pokemon_count = body['count']

    team_members = []
    for i in range(0,6):
        team_members.append(random.randint(1,807))

    team_data = []

    for member in team_members:
        res = requests.get(f"http://pokeapi.co/api/v2/pokemon/{member}/")
        body = json.loads(res.content)
        name = body["name"]
        id = body["id"]
        types = body["types"]

        res1 = requests.get(f"https://api.giphy.com/v1/gifs/random?api_key={key}&tag={name}&rating=g")
        if res1.ok is False:
            return JsonResponse({'status': 'false', 'message': 'Sorry, that api key is invalid'}, status=404)
        body1 = json.loads(res1.content)
        if len(body1['data']) < 1:
            giphy_url = 'Sorry, there are no gifs!'
        else:
            giphy_url = body1['data']['url']

        team_data.append({
        "id": id,
        "name": name,
        "types": types,
        "gif": giphy_url
        })

    return JsonResponse(team_data, safe=False)