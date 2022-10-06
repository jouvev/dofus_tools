class AchievementAchieved:
   def __init__(self,input):
      self._idFunc(input)
      self._achievedByFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + str(self.id) + ") on element of AchievementAchieved.id.")
   
   def _achievedByFunc(self,input) :
      self.achievedBy = input.readVarUhLong()
      if(self.achievedBy < 0 or self.achievedBy > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.achievedBy) + ") on element of AchievementAchieved.achievedBy.")

   def resume(self):
      print("id :",self.id)
      print("achievedBy :",self.achievedBy)
