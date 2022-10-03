class ExchangeShopStockMovementRemovedMessage:
   def __init__(self,input):
      self._objectIdFunc(input)
   
   def _objectIdFunc(self,input) :
      self.objectId = input.readVarUhInt()
      if(self.objectId < 0) :
         raise RuntimeError("Forbidden value (" + self.objectId + ") on element of ExchangeShopStockMovementRemovedMessage.objectId.")