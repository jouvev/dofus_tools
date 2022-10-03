from tmp.types.AchievementAchieved import AchievementAchieved
class AchievementAchievedRewardable(AchievementAchieved):
   def __init__(self,input):
      super().__init__(input)
      self._finishedlevelFunc(input)
   
   def _finishedlevelFunc(self,input) :
      self.finishedlevel = input.readVarUhShort()
      if(self.finishedlevel < 0 or self.finishedlevel > 200) :
         raise RuntimeError("Forbidden value (" + self.finishedlevel + ") on element of AchievementAchievedRewardable.finishedlevel.")