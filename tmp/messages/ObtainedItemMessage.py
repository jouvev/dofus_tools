class ObtainedItemMessage:
   def __init__(self,input):
      self._genericIdFunc(input)
      self._baseQuantityFunc(input)
   
   def _genericIdFunc(self,input) :
      self.genericId = input.readVarUhInt()
      if(self.genericId < 0) :
         raise RuntimeError("Forbidden value (" + self.genericId + ") on element of ObtainedItemMessage.genericId.")
   
   def _baseQuantityFunc(self,input) :
      self.baseQuantity = input.readVarUhInt()
      if(self.baseQuantity < 0) :
         raise RuntimeError("Forbidden value (" + self.baseQuantity + ") on element of ObtainedItemMessage.baseQuantity.")