from tmp.types.GameFightAIInformations import GameFightAIInformations

class GameFightTaxCollectorInformations(GameFightAIInformations):
   def __init__(self,input):
      super().__init__(input)
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
      self._levelFunc(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of GameFightTaxCollectorInformations.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of GameFightTaxCollectorInformations.lastNameId.")
   
   def _levelFunc(self,input) :
      self.level = input.readUnsignedByte()
      if(self.level < 0 or self.level > 255) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameFightTaxCollectorInformations.level.")

   def resume(self):
      super().resume()
      print("firstNameId :",self.firstNameId)
      print("lastNameId :",self.lastNameId)
      print("level :",self.level)
