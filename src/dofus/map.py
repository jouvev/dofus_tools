import json 

class Map:
    mappostmp = json.load(open("ressources/MapPositions.json","r"))
    idtopos = dict()
    for m in mappostmp:
        mapid = m["id"]
        x,y = m["posX"],m["posY"]
        idtopos[mapid] = (x,y)
        
    @classmethod
    def get_pos(cls,mapid):
        if(mapid in cls.idtopos):
            return cls.idtopos[mapid]
        raise RuntimeError(f"Unknown map id {mapid}")