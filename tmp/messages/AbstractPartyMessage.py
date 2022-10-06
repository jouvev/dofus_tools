class AbstractPartyMessage:
   def __init__(self,input):
      self._partyIdFunc(input)
   
   def _partyIdFunc(self,input) :
      self.partyId = input.readVarUhInt()
      if(self.partyId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.partyId) + ") on element of AbstractPartyMessage.partyId.")

   def resume(self):
      print("partyId :",self.partyId)
