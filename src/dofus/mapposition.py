import json 

class MapPosition:
    mapinfo = json.load(open(f"ressources/maps.json","r"))
    mappostmp = json.load(open("ressources/MapPositions.json","r"))
    mappos = dict()
    posmap = dict()
    for m in mappostmp:
        mappos[m["id"]] = m
        
    for m in mappostmp:
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
            linkedzone = int(cls.mapinfo[str(mapid)][str(cellid)]['_linkedZone'])
            return (linkedzone & 240) >> 4
        except:
            raise RuntimeError(f"Error when you tried to got linkedzone on map {mapid}")