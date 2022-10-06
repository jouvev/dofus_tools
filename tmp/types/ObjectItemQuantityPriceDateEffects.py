from tmp.types.ObjectEffects import ObjectEffects
from tmp.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity

class ObjectItemQuantityPriceDateEffects(ObjectItemGenericQuantity):
   def __init__(self,input):
      super().__init__(input)
      self._priceFunc(input)
      self.effects = ObjectEffects(input)
      self._dateFunc(input)
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of ObjectItemQuantityPriceDateEffects.price.")
   
   def _dateFunc(self,input) :
      self.date = input.readInt()
      if(self.date < 0) :
         raise RuntimeError("Forbidden value (" + str(self.date) + ") on element of ObjectItemQuantityPriceDateEffects.date.")

   def resume(self):
      super().resume()
      print("price :",self.price)
      print("date :",self.date)
      self.effects.resum()
