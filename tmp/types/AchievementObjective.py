class AchievementObjective:
   def __init__(self,input):
      self._idFunc(input)
      self._maxValueFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of AchievementObjective.id.")
   
   def _maxValueFunc(self,input) :
      self.maxValue = input.readVarUhShort()
      if(self.maxValue < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxValue) + ") on element of AchievementObjective.maxValue.")

   def resume(self):
      print("id :",self.id)
      print("maxValue :",self.maxValue)
