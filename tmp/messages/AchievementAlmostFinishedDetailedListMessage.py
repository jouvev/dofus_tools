from tmp.types.Achievement import Achievement

class AchievementAlmostFinishedDetailedListMessage:
   def __init__(self,input):
      self.almostFinishedAchievements = []
      _item1 = None
      _almostFinishedAchievementsLen = input.readUnsignedShort()
      for _i1 in range(0,_almostFinishedAchievementsLen):
         _item1 = Achievement(input)
         self.almostFinishedAchievements.append(_item1)

   def resume(self):
      for e in self.almostFinishedAchievements:
         e.resume()
