class ExchangeBidHouseBuyMessage:
   def __init__(self,input):
      self._uidFunc(input)
      self._qtyFunc(input)
      self._priceFunc(input)
   
   def _uidFunc(self,input) :
      self.uid = input.readVarUhInt()
      if(self.uid < 0) :
         raise RuntimeError("Forbidden value (" + self.uid + ") on element of ExchangeBidHouseBuyMessage.uid.")
   
   def _qtyFunc(self,input) :
      self.qty = input.readVarUhInt()
      if(self.qty < 0) :
         raise RuntimeError("Forbidden value (" + self.qty + ") on element of ExchangeBidHouseBuyMessage.qty.")
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.price + ") on element of ExchangeBidHouseBuyMessage.price.")