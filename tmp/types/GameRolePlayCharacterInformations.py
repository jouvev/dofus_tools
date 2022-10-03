from tmp.types.ActorAlignmentInformations import ActorAlignmentInformations
from tmp.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations
class GameRolePlayCharacterInformations(GameRolePlayHumanoidInformations):
   def __init__(self,input):
      super().__init__(input)
      self.alignmentInfos = ActorAlignmentInformations(input)