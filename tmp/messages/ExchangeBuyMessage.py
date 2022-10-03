class ExchangeBuyMessage:
   def __init__(self,input):
      self._objectToBuyIdFunc(input)
      self._quantityFunc(input)
   
   def _objectToBuyIdFunc(self,input) :
      self.objectToBuyId = input.readVarUhInt()
      if(self.objectToBuyId < 0) :
         raise RuntimeError("Forbidden value (" + self.objectToBuyId + ") on element of ExchangeBuyMessage.objectToBuyId.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ExchangeBuyMessage.quantity.")