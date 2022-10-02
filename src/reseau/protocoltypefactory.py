from reseau.protocoltype.fight.GameFightCharacterInformations import GameFightCharacterInformations
from reseau.protocoltype.fight.FightEntityDispositionInformations import FightEntityDispositionInformations
from reseau.protocoltype.fight.GameContextActorPositionInformations import GameContextActorPositionInformations
from reseau.protocoltype.fight.GameFightCharacteristics import GameFightCharacteristics
from reseau.protocoltype.fight.CharacterUsableCharacteristicDetailed import CharacterUsableCharacteristicDetailed
from reseau.protocoltype.fight.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed
from reseau.protocoltype.fight.GameFightMonsterInformations import GameFightMonsterInformations
from reseau.protocoltype.fight.CharacterCharacteristicValue import CharacterCharacteristicValue

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
    