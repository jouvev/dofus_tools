from tmp.types.FightCommonInformations import FightCommonInformations

class GameRolePlayShowChallengeMessage:
   def __init__(self,input):
      self.commonsInfos = FightCommonInformations(input)

   def resume(self):
      self.commonsInfos.resum()
