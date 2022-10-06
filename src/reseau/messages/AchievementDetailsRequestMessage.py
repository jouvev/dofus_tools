class AchievementDetailsRequestMessage:
   def __init__(self,input):
      self._achievementIdFunc(input)
   
   def _achievementIdFunc(self,input) :
      self.achievementId = input.readVarUhShort()
      if(self.achievementId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.achievementId) + ") on element of AchievementDetailsRequestMessage.achievementId.")

   def resume(self):
      print("achievementId :",self.achievementId)
