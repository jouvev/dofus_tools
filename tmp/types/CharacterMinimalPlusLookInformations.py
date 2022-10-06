from tmp.types.EntityLook import EntityLook
from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations

class CharacterMinimalPlusLookInformations(CharacterMinimalInformations):
   def __init__(self,input):
      super().__init__(input)
      self.entityLook = EntityLook(input)
      self._breedFunc(input)
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()

   def resume(self):
      super().resume()
      print("breed :",self.breed)
      self.entityLook.resum()
