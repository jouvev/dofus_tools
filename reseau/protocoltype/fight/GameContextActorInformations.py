from reseau.protocoltype.fight.GameContextActorPositionInformations import GameContextActorPositionInformations
from reseau.protocoltype.fight.EntityLook import EntityLook

class GameContextActorInformations(GameContextActorPositionInformations):
    def __init__(self,content):
        super().__init__(content)
        
        self.look = EntityLook(content)
        
    def resume(self):
        super().resume()
        self.look.resume()