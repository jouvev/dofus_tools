class ExchangeBidHouseGenericItemRemovedMessage:
   def __init__(self,input):
      self._objGenericIdFunc(input)
   
   def _objGenericIdFunc(self,input) :
      self.objGenericId = input.readVarUhInt()
      if(self.objGenericId < 0) :
         raise RuntimeError("Forbidden value (" + self.objGenericId + ") on element of ExchangeBidHouseGenericItemRemovedMessage.objGenericId.")