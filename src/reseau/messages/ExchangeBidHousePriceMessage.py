class ExchangeBidHousePriceMessage:
   def __init__(self,input):
      self._objectGIDFunc(input)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of ExchangeBidHousePriceMessage.objectGID.")

   def resume(self):
      print("objectGID :",self.objectGID)
