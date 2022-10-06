from src.reseau.types.ActorAlignmentInformations import ActorAlignmentInformations
from src.reseau.types.GameFightMonsterInformations import GameFightMonsterInformations

class GameFightMonsterWithAlignmentInformations(GameFightMonsterInformations):
   def __init__(self,input):
      super().__init__(input)
      self.alignmentInfos = ActorAlignmentInformations(input)

   def resume(self):
      super().resume()
      self.alignmentInfos.resum()
