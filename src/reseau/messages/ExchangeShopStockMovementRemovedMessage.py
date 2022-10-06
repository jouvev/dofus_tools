class ExchangeShopStockMovementRemovedMessage:
   def __init__(self,input):
      self._objectIdFunc(input)
   
   def _objectIdFunc(self,input) :
      self.objectId = input.readVarUhInt()
      if(self.objectId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectId) + ") on element of ExchangeShopStockMovementRemovedMessage.objectId.")

   def resume(self):
      print("objectId :",self.objectId)
