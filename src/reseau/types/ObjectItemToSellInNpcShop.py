from src.reseau.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation

class ObjectItemToSellInNpcShop(ObjectItemMinimalInformation):
   def __init__(self,input):
      super().__init__(input)
      self._objectPriceFunc(input)
      self._buyCriterionFunc(input)
   
   def _objectPriceFunc(self,input) :
      self.objectPrice = input.readVarUhLong()
      if(self.objectPrice < 0 or self.objectPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.objectPrice) + ") on element of ObjectItemToSellInNpcShop.objectPrice.")
   
   def _buyCriterionFunc(self,input) :
      self.buyCriterion = input.readUTF()

   def resume(self):
      super().resume()
      print("objectPrice :",self.objectPrice)
      print("buyCriterion :",self.buyCriterion)
