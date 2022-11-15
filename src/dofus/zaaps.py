import json

class Zaaps:
    with open("ressources/zaaps.json", "r",encoding='utf-8') as f:
        zaaps = json.load(f)
        
    @classmethod
    def get_zaaps_by_order(cls,dst,worldmap):
        return sorted([z for z in cls.zaaps if z['worldMapId']==worldmap],key=lambda z:abs(z["x"]-dst[0])+abs(z["y"]-dst[1]))