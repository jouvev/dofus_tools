class AllianceKickRequestMessage:
   def __init__(self,input):
      self._kickedIdFunc(input)
   
   def _kickedIdFunc(self,input) :
      self.kickedId = input.readVarUhInt()
      if(self.kickedId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.kickedId) + ") on element of AllianceKickRequestMessage.kickedId.")

   def resume(self):
      print("kickedId :",self.kickedId)
