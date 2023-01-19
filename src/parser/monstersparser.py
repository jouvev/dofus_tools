import json

monsters = json.load(open("ressources\Monsters.json", "r", encoding="latin-1"))
archi = json.load(open("ressources\\archimonstres.json", "r"))
fr = json.load(open("ressources\i18n_fr.json", "r", encoding="latin-1"))
res = dict()

for m in monsters:
    res[m['id']] = {"name" : fr["texts"][str(m['nameId'])]}
    if(res[m['id']]['name'] in archi):
        res[m['id']]['archi'] = True
    else:
        res[m['id']]['archi'] = False
        
json.dump(res, open("ressources\monsters.json", "w", encoding="latin-1"), indent=4, ensure_ascii=False)