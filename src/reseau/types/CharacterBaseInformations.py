from src.reseau.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations

class CharacterBaseInformations(CharacterMinimalPlusLookInformations):
   def __init__(self,input):
      super().__init__(input)
      self._sexFunc(input)
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()

   def resume(self):
      super().resume()
      print("sex :",self.sex)
