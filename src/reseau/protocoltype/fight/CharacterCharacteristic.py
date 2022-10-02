from binhex import openrsrc
import json

class CharacterCharacteristic:
    def __init__(self,content):
        dico = json.loads(open("ressources/caracid.json","r").read())
        self.caracid = content.readShort()
        self.caracname = dico[str(self.caracid)]
        
    def resume(self):
        print("caracid",self.caracid, "caracname",self.caracname)