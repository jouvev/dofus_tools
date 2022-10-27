from src.chasse.worldhint import WorldHint
from src.chasse.maphint import MapHint
from src.dofus.world import World,MapPosition

w = World.get_instance()
whint = WorldHint()

for s in w.graph.keys():
    map = MapHint(MapPosition.get_pos((s[0])))
    whint.add_node(map)

