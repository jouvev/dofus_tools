class PaddockBuyableInformations:
   def __init__(self,input):
      self._priceFunc(input)
      self._lockedFunc(input)
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of PaddockBuyableInformations.price.")
   
   def _lockedFunc(self,input) :
      self.locked = input.readBoolean()

   def resume(self):
      print("price :",self.price)
      print("locked :",self.locked)
