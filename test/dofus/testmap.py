import json 

path = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\maps\\3333.json"

map = json.load(open(path,"r"))

print(map["layersCount"])
print(map["layers"][1]['cells'][5])