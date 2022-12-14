from src.reseau.types.GameFightFighterLightInformations import GameFightFighterLightInformations

class GameFightFighterTaxCollectorLightInformations(GameFightFighterLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of GameFightFighterTaxCollectorLightInformations.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of GameFightFighterTaxCollectorLightInformations.lastNameId.")

   def resume(self):
      super().resume()
      print("firstNameId :",self.firstNameId)
      print("lastNameId :",self.lastNameId)
