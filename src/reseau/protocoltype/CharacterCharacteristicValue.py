from src.reseau.protocoltype.CharacterCharacteristic import CharacterCharacteristic

class CharacterCharacteristicValue(CharacterCharacteristic):
    def __init__(self,content):
        super().__init__(content)
        self.total = content.readInt()
        
    def resume(self):
        super().resume()
        print("total",self.total)