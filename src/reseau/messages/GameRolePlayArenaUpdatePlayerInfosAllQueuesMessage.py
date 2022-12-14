from src.reseau.messages.GameRolePlayArenaUpdatePlayerInfosMessage import GameRolePlayArenaUpdatePlayerInfosMessage
from src.reseau.types.ArenaRankInfos import ArenaRankInfos
from src.reseau.types.ArenaRankInfos import ArenaRankInfos

class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(GameRolePlayArenaUpdatePlayerInfosMessage):
   def __init__(self,input):
      super().__init__(input)
      self.team = ArenaRankInfos(input)
      self.duel = ArenaRankInfos(input)

   def resume(self):
      super().resume()
      self.team.resume()
      self.duel.resume()
