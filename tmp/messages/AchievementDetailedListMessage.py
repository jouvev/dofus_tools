from tmp.types.Achievement import Achievement
from tmp.types.Achievement import Achievement

class AchievementDetailedListMessage:
   def __init__(self,input):
      self.startedAchievements = []
      self.finishedAchievements = []
      _item1 = None
      _item2 = None
      _startedAchievementsLen = input.readUnsignedShort()
      for _i1 in range(0,_startedAchievementsLen):
         _item1 = Achievement(input)
         self.startedAchievements.append(_item1)
      _finishedAchievementsLen = input.readUnsignedShort()
      for _i2 in range(0,_finishedAchievementsLen):
         _item2 = Achievement(input)
         self.finishedAchievements.append(_item2)

   def resume(self):
      for e in self.startedAchievements:
         e.resume()
      for e in self.finishedAchievements:
         e.resume()
