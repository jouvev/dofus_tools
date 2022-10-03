class PaddockSellRequestMessage:
   def __init__(self,input):
      self._priceFunc(input)
      self._forSaleFunc(input)
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.price + ") on element of PaddockSellRequestMessage.price.")
   
   def _forSaleFunc(self,input) :
      self.forSale = input.readBoolean()