class PaddockBuyRequestMessage:
   def __init__(self,input):
      self._proposedPriceFunc(input)
   
   def _proposedPriceFunc(self,input) :
      self.proposedPrice = input.readVarUhLong()
      if(self.proposedPrice < 0 or self.proposedPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.proposedPrice) + ") on element of PaddockBuyRequestMessage.proposedPrice.")

   def resume(self):
      print("proposedPrice :",self.proposedPrice)
