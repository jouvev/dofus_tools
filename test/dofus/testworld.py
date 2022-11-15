from src.dofus.world import World
from src.chasse.worldhint import WorldHint
from src.dofus.mapposition import MapPosition
import logging

logging.basicConfig(level=logging.INFO)

w = World().get_instance()
whint = WorldHint().get_instance()


"""pos = MapPosition.get_pos("207619076")
print(pos)
print(mapid)
print(MapPosition.posmap[(7,-5,1)])
dep = (mapid, 1.0)
print([(m[0],MapPosition.get_pos(m[0]),w.actions[(dep,m)]) for m in w[dep]])
print(whint.posToNode[(8,-5)].get_left())"""

"""arr = (185863682.0, 1.0)
print(w.actions[dep,arr])"""


dep = (185860609.0,1.0)
arr = (185861634.0,1.0)

print(w.actions[(185862149.0,1.0),(185862148.0,1.0)])

posdep = MapPosition.get_pos(dep[0])
posarr = MapPosition.get_pos(arr[0])

z,p,a = w.get_path((185860609.0,2.0),(-20, -20))
print(z,p,"\n",a)