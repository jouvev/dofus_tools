from src.reseau.protocoltype.CharacterCharacteristic import CharacterCharacteristic

class CharacterCharacteristicDetailed(CharacterCharacteristic):
    def __init__(self,content):
        super().__init__(content)
        self.base = content.readVarInt()
        self.additional = content.readVarInt()
        self.objectsandmountbonus = content.readVarInt()
        self.alignementbonus = content.readVarInt()
        self.contextmodif = content.readVarInt()
        
        
    def resume(self):
        super().resume()
        print("base",self.base)
        print('additional',self.additional)
        print('objectsandmountbonus',self.objectsandmountbonus)
        print('alignementbonus',self.alignementbonus)
        print('contextmodif',self.contextmodif)
        