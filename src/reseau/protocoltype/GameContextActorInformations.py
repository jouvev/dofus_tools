from src.reseau.protocoltype.GameContextActorPositionInformations import GameContextActorPositionInformations
from src.reseau.protocoltype.EntityLook import EntityLook

class GameContextActorInformations(GameContextActorPositionInformations):
    def __init__(self,content):
        super().__init__(content)
        
        self.look = EntityLook(content)
        
    def resume(self):
        super().resume()
        self.look.resume()