import requests
import json

key = json.load(open("ressources/apikeys.json", "r"))["HTTP-X-APIKEY"]
header = {"HTTP-X-APIKEY": key}

res = requests.get("http://api.metamob.fr/monstres?type=archimonstre", headers=header).json()

print(res)

namesArchi = [i["nom"] for i in res]

json.dump(namesArchi,open("ressources/archimonstres.json", "w", encoding="utf-8"),indent=2 ,ensure_ascii=False)