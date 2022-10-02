from reseau.protocoltype.fight.CharacterCharacteristics import CharacterCharacteristics

class GameFightCharacteristics:
    def __init__(self,content):
        self.carac = CharacterCharacteristics(content)
        self.summoner = content.readDouble()
        self.summoned = content.readBoolean()
        self.inviState = content.readByte()
        
        
    def resume(self):
        self.carac.resume()
        print("summoner",self.summoner)
        print("summoned",self.summoned)
        print("inviState",self.inviState)