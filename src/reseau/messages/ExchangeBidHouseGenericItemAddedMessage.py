class ExchangeBidHouseGenericItemAddedMessage:
   def __init__(self,input):
      self._objGenericIdFunc(input)
   
   def _objGenericIdFunc(self,input) :
      self.objGenericId = input.readVarUhInt()
      if(self.objGenericId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objGenericId) + ") on element of ExchangeBidHouseGenericItemAddedMessage.objGenericId.")

   def resume(self):
      print("objGenericId :",self.objGenericId)
