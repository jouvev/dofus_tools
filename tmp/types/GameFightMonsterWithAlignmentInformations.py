from tmp.types.ActorAlignmentInformations import ActorAlignmentInformations
from tmp.types.GameFightMonsterInformations import GameFightMonsterInformations
class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
   def __init__(self,input):
      super().__init__(input)
      self.alignmentInfos = ActorAlignmentInformations(input)