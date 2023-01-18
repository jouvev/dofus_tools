import json 

CAPABILITY_ALLOW_TELEPORT_TO = 4

class MapPosition:
    with open(f"ressources/maps.json","r") as file:
        mapinfo = json.load(file)
    with open("ressources/MapPositions.json","r") as file:
        mappostmp = json.load(file)
    mappos = dict()
    posmap = dict()
    for m in mappostmp:
        mappos[m["id"]] = m
        
    for m in mappostmp:
        if((m["posX"],m["posY"],m["worldMap"]) in posmap):
            if(m["hasPriorityOnWorldmap"]==True):
                posmap[(m["posX"],m["posY"],m["worldMap"])] = m
        else:
            posmap[(m["posX"],m["posY"],m["worldMap"])] = m
        
    @classmethod
    def get_pos(cls,mapid):
        if(mapid in cls.mappos):
            return cls.mappos[mapid]["posX"],cls.mappos[mapid]["posY"]
        raise RuntimeError(f"Unknown map id {mapid}")
    
    @classmethod
    def get_worldmap(cls,mapid):
        if(mapid in cls.mappos):
            return cls.mappos[mapid]["worldMap"]
        raise RuntimeError(f"Unknown map id {mapid}")
    
    @classmethod
    def get_mapid(cls,x,y,worldmap):
        entry = (int(x),int(y),worldmap)
        if(entry in cls.posmap):
            return cls.posmap[entry]["id"]
        raise RuntimeError(f"Unknown map pos {entry}")
    
    @classmethod
    def get_linkedzone(cls,mapid,cellid):
        try :
            linkedzone = int(cls.mapinfo[str(int(mapid))][str(cellid)]['_linkedZone'])
            return (linkedzone & 240) >> 4
        except:
            raise RuntimeError(f"Error when you tried to got linkedzone on map {mapid}")
        
    @classmethod
    def can_havresac(cls,mapid):
        return True#cls.mappos[mapid]["capabilities"] & CAPABILITY_ALLOW_TELEPORT_TO != 0