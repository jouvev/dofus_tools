from tmp.types.GameFightFighterLightInformations import GameFightFighterLightInformations
class GameFightFighterTaxCollectorLightInformations(GameFightFighterLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + self.firstNameId + ") on element of GameFightFighterTaxCollectorLightInformations.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + self.lastNameId + ") on element of GameFightFighterTaxCollectorLightInformations.lastNameId.")