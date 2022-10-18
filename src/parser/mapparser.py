import os
import json

def get_all_path(root_path):
    script_path = []
    for root, dirs, files in os.walk(root_path): 
        path = root.split(os.sep)
        for f in files:
            if(f.endswith(".dlm")):
                script_path.append(os.path.join(*path,f))
    return script_path

finalres = dict()

output_path = "C:/Users/vincent/Desktop/dofus_source/PyDofus-master/PyDofus-master/output/maps"
allpath = get_all_path("C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\input")
print(len(allpath))
for i,p in enumerate(allpath):
    p = p.replace("\\","/")
    print(f"{i}/{len(allpath)} => {p}")
    fichiername = p.split("/")[-1].replace(".dlm",".json")
    os.system(f"python C:/Users/vincent/Desktop/dofus_source/PyDofus-master/PyDofus-master/dlm_unpack.py {p} {output_path}")
    outputfichier = os.path.join(output_path,fichiername)
    with open(outputfichier,"r") as f:
        res = json.load(f)
        mapid = res["mapId"]
        cellstmp = res["cells"]
        cells = dict()
        for j,ctmp in enumerate(cellstmp):
            if("_linkedZone" in ctmp):
                c = dict()
                c["_linkedZone"] = ctmp["_linkedZone"]
                cells[j] = c
        finalres[mapid] = cells
        
json.dump(finalres,open("D:\\Documents\\GitHub\\outils_dofus\\ressources\\maps.json","w"))