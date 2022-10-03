class ExchangeSellMessage:
   def __init__(self,input):
      self._objectToSellIdFunc(input)
      self._quantityFunc(input)
   
   def _objectToSellIdFunc(self,input) :
      self.objectToSellId = input.readVarUhInt()
      if(self.objectToSellId < 0) :
         raise RuntimeError("Forbidden value (" + self.objectToSellId + ") on element of ExchangeSellMessage.objectToSellId.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ExchangeSellMessage.quantity.")