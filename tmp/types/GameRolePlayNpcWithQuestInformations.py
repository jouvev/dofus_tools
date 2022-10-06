from tmp.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from tmp.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations

class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
   def __init__(self,input):
      super().__init__(input)
      self.questFlag = GameRolePlayNpcQuestFlag(input)

   def resume(self):
      super().resume()
      self.questFlag.resum()
