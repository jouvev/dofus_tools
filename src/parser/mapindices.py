import json
import os

path = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\maps"

mapidworl1 = [str(m["id"])[:-2] for m in json.load(open("ressources\\MapPositions.json")) if m["worldMap"] == 1]
listeworld1 = [jsonname for jsonname in os.listdir(path) if jsonname[:-5] in mapidworl1]

edict = dict()
tfidf = dict()


for i,jsonname in enumerate(listeworld1):
    if(i%100 == 0):
        print(f"{i}/{len(listeworld1)}")
        
    pathjson = os.path.join(path, jsonname)
    mapinfo = json.load(open(pathjson))
    
    cells = []
    for l in mapinfo["layers"]:
        cells += l["cells"]
    
    elem = []
    for c in cells:
        elem += c["elements"]
        
    elem = [e for e in elem if e["elementName"]=="Graphical"]
    
    for e in elem:
        eid = str(e["elementId"])
        if(eid in edict):
            edict[eid] += 1
            if jsonname[:-5] in tfidf[eid]:
                tfidf[eid][jsonname[:-5]] += 1
            else:
                tfidf[eid][jsonname[:-5]] = 1
        else:
            edict[eid] = 1
            tfidf[eid] = {jsonname[:-5]:1}
            
            
json.dump(edict, open("ressources\\mapelem.json", "w"),indent=2)
json.dump(tfidf, open("ressources\\tfidf.json", "w"),indent=2)