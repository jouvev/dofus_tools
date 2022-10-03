class AbstractPartyMessage:
   def __init__(self,input):
      self._partyIdFunc(input)
   
   def _partyIdFunc(self,input) :
      self.partyId = input.readVarUhInt()
      if(self.partyId < 0) :
         raise RuntimeError("Forbidden value (" + self.partyId + ") on element of AbstractPartyMessage.partyId.")