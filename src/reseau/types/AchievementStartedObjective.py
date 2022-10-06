from src.reseau.types.AchievementObjective import AchievementObjective

class AchievementStartedObjective(AchievementObjective):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readVarUhShort()
      if(self.value < 0) :
         raise RuntimeError("Forbidden value (" + str(self.value) + ") on element of AchievementStartedObjective.value.")

   def resume(self):
      super().resume()
      print("value :",self.value)
