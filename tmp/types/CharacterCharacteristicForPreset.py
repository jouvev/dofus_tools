from tmp.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset

class CharacterCharacteristicForPreset(SimpleCharacterCharacteristicForPreset):
   def __init__(self,input):
      super().__init__(input)
      self._stuffFunc(input)
   
   def _stuffFunc(self,input) :
      self.stuff = input.readVarInt()

   def resume(self):
      super().resume()
      print("stuff :",self.stuff)
