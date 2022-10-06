from tmp.types.ObjectItemToSell import ObjectItemToSell

class ObjectItemToSellInBid(ObjectItemToSell):
   def __init__(self,input):
      super().__init__(input)
      self._unsoldDelayFunc(input)
   
   def _unsoldDelayFunc(self,input) :
      self.unsoldDelay = input.readInt()
      if(self.unsoldDelay < 0) :
         raise RuntimeError("Forbidden value (" + str(self.unsoldDelay) + ") on element of ObjectItemToSellInBid.unsoldDelay.")

   def resume(self):
      super().resume()
      print("unsoldDelay :",self.unsoldDelay)
