class PaddockSellBuyDialogMessage:
   def __init__(self,input):
      self._bsellFunc(input)
      self._ownerIdFunc(input)
      self._priceFunc(input)
   
   def _bsellFunc(self,input) :
      self.bsell = input.readBoolean()
   
   def _ownerIdFunc(self,input) :
      self.ownerId = input.readVarUhInt()
      if(self.ownerId < 0) :
         raise RuntimeError("Forbidden value (" + self.ownerId + ") on element of PaddockSellBuyDialogMessage.ownerId.")
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.price + ") on element of PaddockSellBuyDialogMessage.price.")