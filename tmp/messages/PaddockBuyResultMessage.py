class PaddockBuyResultMessage:
   def __init__(self,input):
      self._paddockIdFunc(input)
      self._boughtFunc(input)
      self._realPriceFunc(input)
   
   def _paddockIdFunc(self,input) :
      self.paddockId = input.readDouble()
      if(self.paddockId < 0 or self.paddockId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.paddockId + ") on element of PaddockBuyResultMessage.paddockId.")
   
   def _boughtFunc(self,input) :
      self.bought = input.readBoolean()
   
   def _realPriceFunc(self,input) :
      self.realPrice = input.readVarUhLong()
      if(self.realPrice < 0 or self.realPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.realPrice + ") on element of PaddockBuyResultMessage.realPrice.")