class MapRunningFightDetailsRequestMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of MapRunningFightDetailsRequestMessage.fightId.")

   def resume(self):
      print("fightId :",self.fightId)
