from tmp.types.AchievementAchievedRewardable import AchievementAchievedRewardable
class AchievementFinishedMessage:
   def __init__(self,input):
      self.achievement = AchievementAchievedRewardable(input)