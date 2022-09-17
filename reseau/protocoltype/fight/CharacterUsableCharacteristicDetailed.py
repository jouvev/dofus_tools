from reseau.protocoltype.fight.CharacterCharacteristicDetailed import CharacterCharacteristicDetailed

class CharacterUsableCharacteristicDetailed(CharacterCharacteristicDetailed):
    def __init__(self,content):
        super().__init__(content)
        self.used = content.readVarInt()
        
    def resume(self):
        super().resume()
        print('used',self.used)