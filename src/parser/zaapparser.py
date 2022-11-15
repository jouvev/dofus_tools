import json

path = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\common\\Hints.json"
suba_path = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\common\\SubAreas.json"
i18n_fr_path = "D:\\Documents\\GitHub\\outils_dofus\\ressources\\i18n_fr.json"

savedZaaps = [88212481.0,
    173278210.0,
    156762120.0,
    142087694.0,
    207619076.0,
    88082704.0,
    164364304.0,
    165152263.0,
    191105026.0,
    115083777.0,
    54172969.0,
    147590153.0,
    154642.0,
    88212746.0,
    212861955.0,
    95422468.0,
    68419587.0,
    73400320.0,
    88213271.0,
    68552706.0,
    185860609.0,
    88085249.0,
    20973313.0,
    156240386.0,
    171967506.0,
    120062979.0,
    212600323.0,
    99615238.0,
    121634816.0,
    129368579.0,
    84806401.0]

with open(path, "r") as f:
    data = json.load(f)
    
with open(suba_path, "r") as f:
    suba = json.load(f)
    
subatmp = dict()
for sa in suba:
    subatmp[sa["id"]] = sa["nameId"]
    
with open(i18n_fr_path, "r", encoding="utf-8") as f:
    i18n_fr = json.load(f)['texts']
    
res = []
for d in data :
    if(d['gfx'] == 410):
        subid = d['subareaId']
        namesuba = i18n_fr[str(subatmp[subid])]
        d['name'] = namesuba
        d['zone'] = 1
        del d['categoryId']
        del d['gfx']
        del d["nameId"]
        del d['realMapId']
        del d['outdoor']
        del d['subareaId']
        del d['level']
        if(d['mapId'] in savedZaaps):
            res.append(d)
        else:
            print(d['name'],"supp")

print(len(res))
json.dump(res,open("D:\\Documents\\GitHub\\outils_dofus\\ressources\\zaaps.json","w",encoding="utf-8"),indent=3,ensure_ascii=False)