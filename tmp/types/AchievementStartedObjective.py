from tmp.types.AchievementObjective import AchievementObjective
class AchievementStartedObjective(AchievementObjective):
   def __init__(self,input):
      super().__init__(input)
      self._valueFunc(input)
   
   def _valueFunc(self,input) :
      self.value = input.readVarUhShort()
      if(self.value < 0) :
         raise RuntimeError("Forbidden value (" + self.value + ") on element of AchievementStartedObjective.value.")