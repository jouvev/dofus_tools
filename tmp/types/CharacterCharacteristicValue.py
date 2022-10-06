from tmp.types.CharacterCharacteristic import CharacterCharacteristic

class CharacterCharacteristicValue(CharacterCharacteristic):
   def __init__(self,input):
      super().__init__(input)
      self._totalFunc(input)
   
   def _totalFunc(self,input) :
      self.total = input.readInt()

   def resume(self):
      super().resume()
      print("total :",self.total)
