from reseau.protocoltype.fight.GameFightFighterInformations import GameFightFighterInformations

class GameFightAIInformations(GameFightFighterInformations):
    def __init__(self,content):
        super().__init__(content)
        
    def resume(self):
        super().resume()