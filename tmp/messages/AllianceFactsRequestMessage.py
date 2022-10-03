class AllianceFactsRequestMessage:
   def __init__(self,input):
      self._allianceIdFunc(input)
   
   def _allianceIdFunc(self,input) :
      self.allianceId = input.readVarUhInt()
      if(self.allianceId < 0) :
         raise RuntimeError("Forbidden value (" + self.allianceId + ") on element of AllianceFactsRequestMessage.allianceId.")