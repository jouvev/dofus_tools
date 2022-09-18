from reseau.messages.fight.GameFightSynchronizeMessage import GameFightSynchronizeMessage
from reseau.messages.fight.GameFightTurnListMessage import GameFightTurnListMessage
import json

class MessageFactory:
    id_class = json.load(open('reseau/id_class.json'))
    
    @classmethod
    def get_instance_id(cls,id,content):
        classname = cls.id_class[str(id)].split('.')[-1]
        return cls.get_instance_classname(classname,content)
    
    @classmethod
    def get_instance_classname(cls,classname,content):
        if(classname == "GameFightSynchronizeMessage"):
            return GameFightSynchronizeMessage(content)
        elif(classname == "GameFightTurnListMessage"):
            return GameFightTurnListMessage(content)
        else :
            raise RuntimeError(classname+' not implemented')
        