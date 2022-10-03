class ExchangeBidPriceMessage:
   def __init__(self,input):
      self._genericIdFunc(input)
      self._averagePriceFunc(input)
   
   def _genericIdFunc(self,input) :
      self.genericId = input.readVarUhInt()
      if(self.genericId < 0) :
         raise RuntimeError("Forbidden value (" + self.genericId + ") on element of ExchangeBidPriceMessage.genericId.")
   
   def _averagePriceFunc(self,input) :
      self.averagePrice = input.readVarLong()
      if(self.averagePrice < -9007199254740992 or self.averagePrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.averagePrice + ") on element of ExchangeBidPriceMessage.averagePrice.")