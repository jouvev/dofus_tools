import json

class Monstre:
    infos = json.load(open("ressources\monsters.json", "r", encoding="latin-1"))
    
    @classmethod
    def is_archi(cls, id):
        return cls.infos[id]["archi"]