from src.chasse.worldhint import WorldHint
from src.chasse.maphint import MapHint
from src.dofus.world import World,MapPosition
import json

w = World.get_instance()
whint = WorldHint()

#créer tout les noeuds
for s in w.graph.keys():
    try:
        if(MapPosition.get_worldmap(s[0]) == 1):
            map = MapHint(MapPosition.get_pos(s[0]))
            whint.add_node(map)
    except RuntimeError:
        continue
    
print(len(whint.posToNode))
print(whint.get_node((-81,-37)).get_pos())
    
#connecter les noeuds
for s in w.graph.keys():
    try:
        if(MapPosition.get_worldmap(s[0]) == 1):
            for voisin in w.graph[s]:
                if(MapPosition.get_pos(voisin[0]) in whint.posToNode and w.actions[(s,voisin)][0] in [0,2,4,6]):
                    whint.add_map_direction(MapPosition.get_pos(s[0]),w.actions[(s,voisin)][0],MapPosition.get_pos(voisin[0]))
    except RuntimeError:
        continue

print(whint.posToNode[(-81,-37)].get_right())
print(whint.posToNode[(-5,-8)].get_right())
print(whint.posToNode[(-5,-8)].get_left())
print(whint.posToNode[(-5,-8)].get_down())
print(whint.posToNode[(-5,-8)].get_up())

idname = json.load(open('D:\\Téléchargement\\idname.json',encoding='utf-8'))
idname = {e['clueid']:e['hintfr'] for e in idname}
pos = json.load(open('D:\\Téléchargement\\huntlist.json',encoding='utf-8'))

for m in pos:
    x,y = m['x'],m['y']
    for i in m['clues']:
        hint = idname[i]
        whint.posToNode[(int(x),int(y))].add_hint(hint)
    
print(whint.posToNode[(-2,0)].get_hints())
print(whint.posToNode[(-2,0)].get_right())
print(whint.get_hint((-3,0),0,"Blé noir et blanc"))
whint.sereliaze()