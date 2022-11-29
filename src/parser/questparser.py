import json 

path = "C:\\Users\\vincent\\Desktop\\dofus_source\\PyDofus-master\\PyDofus-master\\output\\common\\QuestObjectives.json"

with open(path,"r") as f:
    questobjective = json.load(f)

questres = dict()

for q in questobjective:
    questres[q["stepId"]] = {"id":q["id"],"mapid":q["mapId"]}

json.dump(questres,open("ressources\\questObjectives.json","w"))