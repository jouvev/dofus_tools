from src.reseau.types.Achievement import Achievement

class AchievementDetailsMessage:
   def __init__(self,input):
      self.achievement = Achievement(input)

   def resume(self):
      self.achievement.resum()
