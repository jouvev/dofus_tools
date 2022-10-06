from tmp.types.Item import Item

class GoldItem(Item):
   def __init__(self,input):
      super().__init__(input)
      self._sumFunc(input)
   
   def _sumFunc(self,input) :
      self.sum = input.readVarUhLong()
      if(self.sum < 0 or self.sum > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sum) + ") on element of GoldItem.sum.")

   def resume(self):
      super().resume()
      print("sum :",self.sum)
