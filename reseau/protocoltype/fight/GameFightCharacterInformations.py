from reseau.protocoltype.fight.GameFightFighterNamedInformations import GameFightFighterNamedInformations
from reseau.protocoltype.fight.ActorAlignmentInformations import ActorAlignmentInformations

class GameFightCharacterInformations(GameFightFighterNamedInformations):
    def __init__(self,content):
        super().__init__(content)
        self.level = content.readVarShort()
        self.alignement = ActorAlignmentInformations(content)
        self.breed = content.readByte()
        self.sex = content.readBoolean()
        
        
    def resume(self):
        super().resume()
        print("level",self.level)
        self.alignement.resume()
        print("breed",self.breed)
        print("sex",self.sex)
        