from tmp.types.HumanOption import HumanOption

class HumanOptionSpeedMultiplier(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._speedMultiplierFunc(input)
   
   def _speedMultiplierFunc(self,input) :
      self.speedMultiplier = input.readVarUhInt()
      if(self.speedMultiplier < 0) :
         raise RuntimeError("Forbidden value (" + str(self.speedMultiplier) + ") on element of HumanOptionSpeedMultiplier.speedMultiplier.")

   def resume(self):
      super().resume()
      print("speedMultiplier :",self.speedMultiplier)
