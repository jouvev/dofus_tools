from src.reseau.protocoltype.GameFightAIInformations import GameFightAIInformations

class GameFightMonsterInformations(GameFightAIInformations):
    def __init__(self,content):
        super().__init__(content)
        self.creaGen = content.readVarShort()
        self.creaGrade = content.readByte()
        self.creatureLevel = content.readShort()
        
    def resume(self):
        super().resume()
        print("creaGen",self.creaGen)
        print("creaGrade",self.creaGrade)
        print("level creature",self.creatureLevel)