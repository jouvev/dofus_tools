from src.reseau.types.EntityDispositionInformations import EntityDispositionInformations

class FightEntityDispositionInformations(EntityDispositionInformations):
   def __init__(self,input):
      super().__init__(input)
      self._carryingCharacterIdFunc(input)
   
   def _carryingCharacterIdFunc(self,input) :
      self.carryingCharacterId = input.readDouble()
      if(self.carryingCharacterId < -9007199254740992 or self.carryingCharacterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.carryingCharacterId) + ") on element of FightEntityDispositionInformations.carryingCharacterId.")

   def resume(self):
      super().resume()
      print("carryingCharacterId :",self.carryingCharacterId)
