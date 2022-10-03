class AllianceKickRequestMessage:
   def __init__(self,input):
      self._kickedIdFunc(input)
   
   def _kickedIdFunc(self,input) :
      self.kickedId = input.readVarUhInt()
      if(self.kickedId < 0) :
         raise RuntimeError("Forbidden value (" + self.kickedId + ") on element of AllianceKickRequestMessage.kickedId.")