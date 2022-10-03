from src.reseau.protocoltype.GameFightCharacterInformations import GameFightCharacterInformations
from src.reseau.protocoltype.FightEntityDispositionInformations import FightEntityDispositionInformations
from src.reseau.protocoltype.GameContextActorPositionInformations import GameContextActorPositionInformations
from src.reseau.protocoltype.GameFightCharacteristics import GameFightCharacteristics
from src.reseau.protocoltype.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from src.reseau.protocoltype.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from src.reseau.protocoltype.GameFightMonsterInformations import GameFightMonsterInformations
from src.reseau.protocoltype.CharacterCharacteristicValue import CharacterCharacteristicValue

import json

class ProtocolTypeFactory:
    id_class = json.load(open('ressources/id_protocol.json'))
    
    @classmethod
    def get_instance_id(cls,id,content):
        classname = cls.id_class[str(id)].split('.')[-1]
        return cls.get_instance_classname(classname,content)
    
    @classmethod
    def get_instance_classname(cls,classname,content):
        if(classname == "GameFightCharacterInformations"):
            return GameFightCharacterInformations(content)
        elif(classname == "FightEntityDispositionInformations"):
            return FightEntityDispositionInformations(content)
        elif(classname == "GameContextActorPositionInformations"):
            return GameContextActorPositionInformations(content)
        elif(classname == "GameFightCharacteristics"):
            return GameFightCharacteristics(content)
        elif(classname == "CharacterUsableCharacteristicDetailed"):
            return CharacterUsableCharacteristicDetailed(content)
        elif(classname == "CharacterCharacteristicDetailed"):
            return CharacterCharacteristicDetailed(content)
        elif(classname == "GameFightMonsterInformations"):
            return GameFightMonsterInformations(content)
        elif(classname == "CharacterCharacteristicValue"):
            return CharacterCharacteristicValue(content)
        else :
            raise RuntimeError(classname+' not implemented')
    