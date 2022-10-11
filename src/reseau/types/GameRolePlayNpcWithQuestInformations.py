from src.reseau.types.GameRolePlayNpcQuestFlag import GameRolePlayNpcQuestFlag
from src.reseau.types.GameRolePlayNpcInformations import GameRolePlayNpcInformations

class GameRolePlayNpcWithQuestInformations(GameRolePlayNpcInformations):
   def __init__(self,input):
      super().__init__(input)
      self.questFlag = GameRolePlayNpcQuestFlag(input)

   def resume(self):
      super().resume()
      self.questFlag.resume()
