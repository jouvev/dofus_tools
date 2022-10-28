from src.chasse.worldhint import WorldHint
from src.chasse.maphint import MapHint
from src.dofus.world import World,MapPosition
import json
import unidecode

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
    
#connecter les noeuds
for s in w.graph.keys():
    try:
        xs,ys = MapPosition.get_pos(s[0])
        if(MapPosition.get_worldmap(s[0]) == 1 and MapPosition.posmap[(xs,ys,1)]['id'] == s[0]):
            for voisin in w.graph[s]:
                xvoisin,yvoisin = MapPosition.get_pos(voisin[0])
                if(MapPosition.get_worldmap(voisin[0]) == 1 and
                   MapPosition.posmap[(xvoisin,yvoisin,1)]['id'] == voisin[0] and 
                   w.actions[(s,voisin)][0] in [0,2,4,6]):
                    whint.add_map_direction(MapPosition.get_pos(s[0]),w.actions[(s,voisin)][0],MapPosition.get_pos(voisin[0]))
    except RuntimeError:
        continue

idname = json.load(open('ressources\\idname.json',encoding='utf-8'))
idname = {e['clueid']:e['hintfr'] for e in idname}
pos = json.load(open('ressources\\huntlist.json',encoding='utf-8'))

for m in pos:
    x,y = m['x'],m['y']
    for i in m['clues']:
        hint = unidecode.unidecode(idname[i].lower())
        whint.posToNode[(int(x),int(y))].add_hint(hint)
    
print('save')
whint.sereliaze()