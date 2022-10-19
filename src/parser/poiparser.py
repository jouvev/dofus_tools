import json 

pois = json.load(open("C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\common\\PointOfInterest.json"))
trad = json.load(open("ressources\\i18n_fr.json",encoding='utf-8'))['texts']

res = {str(poi['id']): trad[str(poi['nameId'])] for poi in pois} 

print(res)

json.dump(res, open("ressources\\poi.json", "w", encoding="utf-8"),indent=3,ensure_ascii=False)