from src.dofus.world import World
from src.dofus.mapposition import MapPosition
import logging

logging.basicConfig(level=logging.INFO)

w = World()
w.deserialize()

dep = (185860609.0,1.0)
arr = (185861634.0,1.0)

print(w.actions[(88082192.0,1.0),(88081680.0,1.0)])

posdep = MapPosition.get_pos(dep[0])
posarr = MapPosition.get_pos(arr[0])

p,a = w.findpath((185860609.0,2.0),(185861634.0,1.0))

print(f"{posdep} => {posarr}")
print([MapPosition.get_pos(x[0]) for x in p])
print(a)

test2 = (193331717.0,1.0)
print(w[test2])