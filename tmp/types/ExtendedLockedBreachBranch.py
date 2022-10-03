from tmp.types.ExtendedBreachBranch import ExtendedBreachBranch
class ExtendedLockedBreachBranch(ExtendedBreachBranch):
   def __init__(self,input):
      super().__init__(input)
      self._unlockPriceFunc(input)
   
   def _unlockPriceFunc(self,input) :
      self.unlockPrice = input.readVarUhInt()
      if(self.unlockPrice < 0) :
         raise RuntimeError("Forbidden value (" + self.unlockPrice + ") on element of ExtendedLockedBreachBranch.unlockPrice.")