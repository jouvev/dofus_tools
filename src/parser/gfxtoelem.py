import json 
import pickle

elem = json.load(open("C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\elements.json"))["elements_map"]
i,gfxpoi = pickle.load(open("tmp\\backup.pkl","rb"))

def gfxtoelemid(gfxid):
    res = []
    for eid,e in elem.items():
        if 'gfx_id' in e and str(e["gfx_id"]) == gfxid:
            res.append(e["id"])
    return res

elemidpoi = dict()
for g,poi in gfxpoi.items():
    elemids = gfxtoelemid(g)
    for e in elemids:
        elemidpoi[e] = poi
        
print(elemidpoi)
        
json.dump(elemidpoi,open("ressources\\elemidpoi.json","w",encoding="utf-8"),indent=2,ensure_ascii=False)