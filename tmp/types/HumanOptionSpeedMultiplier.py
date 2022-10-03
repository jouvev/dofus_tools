from tmp.types.HumanOption import HumanOption
class HumanOptionSpeedMultiplier(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._speedMultiplierFunc(input)
   
   def _speedMultiplierFunc(self,input) :
      self.speedMultiplier = input.readVarUhInt()
      if(self.speedMultiplier < 0) :
         raise RuntimeError("Forbidden value (" + self.speedMultiplier + ") on element of HumanOptionSpeedMultiplier.speedMultiplier.")