from tmp.messages.ExchangeBidPriceMessage import ExchangeBidPriceMessage

class ExchangeBidPriceForSellerMessage(ExchangeBidPriceMessage):
   def __init__(self,input):
      self.minimalPrices = []
      _val2 = None
      super().__init__(input)
      self._allIdenticalFunc(input)
      _minimalPricesLen = input.readUnsignedShort()
      for _i2 in range(0,_minimalPricesLen):
         _val2 = input.readVarUhLong()
         if(_val2 < 0 or _val2 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of minimalPrices.")
         self.minimalPrices.append(_val2)
   
   def _allIdenticalFunc(self,input) :
      self.allIdentical = input.readBoolean()

   def resume(self):
      super().resume()
      print("allIdentical :",self.allIdentical)
      print("minimalPrices :",self.minimalPrices)
