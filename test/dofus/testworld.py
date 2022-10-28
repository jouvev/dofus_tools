from src.dofus.world import World
from src.chasse.worldhint import WorldHint
from src.dofus.mapposition import MapPosition
import logging

logging.basicConfig(level=logging.INFO)

w = World().get_instance()
whint = WorldHint().get_instance()


mapid = MapPosition.get_mapid(0,0,1)
print(mapid)
print(MapPosition.mappos[mapid])
dep = (mapid, 1.0)
print([(m[0],MapPosition.get_pos(m[0]),w.actions[(dep,m)]) for m in w[dep]])
print(whint.posToNode[(0,0)].get_right())

"""arr = (185863682.0, 1.0)
print(w.actions[dep,arr])"""

"""dep = (185860609.0,1.0)
arr = (185861634.0,1.0)

print(w.actions[(185862149.0,1.0),(185862148.0,1.0)])"""

"""posdep = MapPosition.get_pos(dep[0])
posarr = MapPosition.get_pos(arr[0])

p,a = w.findpath((185860609.0,2.0),(185861634.0,1.0))

print(f"{posdep} => {posarr}")
print([MapPosition.get_pos(x[0]) for x in p])
print(a)

test2 = (193331717.0,1.0)
print(w[test2])"""