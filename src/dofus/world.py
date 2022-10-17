from src.dofus.map import Map

class Node:
    def __init__(self, mapid):
        self.mapid = mapid
        self.x, self.y = Map.get_pos(mapid)
        