from src.reseau.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage

class MapComplementaryInformationsAnomalyMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      super().__init__(input)
      self._levelFunc(input)
      self._closingTimeFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of MapComplementaryInformationsAnomalyMessage.level.")
   
   def _closingTimeFunc(self,input) :
      self.closingTime = input.readVarUhLong()
      if(self.closingTime < 0 or self.closingTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.closingTime) + ") on element of MapComplementaryInformationsAnomalyMessage.closingTime.")

   def resume(self):
      super().resume()
      print("level :",self.level)
      print("closingTime :",self.closingTime)
