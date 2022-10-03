class ExchangeBidHouseListMessage:
   def __init__(self,input):
      self._objectGIDFunc(input)
      self._followFunc(input)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ExchangeBidHouseListMessage.objectGID.")
   
   def _followFunc(self,input) :
      self.follow = input.readBoolean()