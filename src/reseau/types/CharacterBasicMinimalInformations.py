from src.reseau.types.AbstractCharacterInformation import AbstractCharacterInformation

class CharacterBasicMinimalInformations(AbstractCharacterInformation):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()

   def resume(self):
      super().resume()
      print("name :",self.name)
