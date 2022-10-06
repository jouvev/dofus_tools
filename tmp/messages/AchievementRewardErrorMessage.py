class AchievementRewardErrorMessage:
   def __init__(self,input):
      self._achievementIdFunc(input)
   
   def _achievementIdFunc(self,input) :
      self.achievementId = input.readShort()

   def resume(self):
      print("achievementId :",self.achievementId)
