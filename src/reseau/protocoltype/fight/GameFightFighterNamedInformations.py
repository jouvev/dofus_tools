from reseau.protocoltype.fight.GameFightFighterInformations import GameFightFighterInformations
from reseau.protocoltype.fight.PlayerStatus import PlayerStatus

class GameFightFighterNamedInformations(GameFightFighterInformations):
    def __init__(self,content):
        super().__init__(content)
        self.name = content.readUTF()
        self.status = PlayerStatus(content)
        self.leagueId = content.readVarShort()
        self.ladderPosition = content.readInt()
        self.hiddenInPrefight = content.readBoolean()
        
    def resume(self):
        super().resume()
        print("name",self.name)
        self.status.resume()
        print("leagueId",self.leagueId)
        print("ladderPosition",self.ladderPosition)
        print("hiddenInPrefight",self.hiddenInPrefight)