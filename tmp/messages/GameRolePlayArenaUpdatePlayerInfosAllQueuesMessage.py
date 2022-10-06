from tmp.messages.GameRolePlayArenaUpdatePlayerInfosMessage import GameRolePlayArenaUpdatePlayerInfosMessage
from tmp.types.ArenaRankInfos import ArenaRankInfos
from tmp.types.ArenaRankInfos import ArenaRankInfos

class GameRolePlayArenaUpdatePlayerInfosAllQueuesMessage(GameRolePlayArenaUpdatePlayerInfosMessage):
   def __init__(self,input):
      super().__init__(input)
      self.team = ArenaRankInfos(input)
      self.duel = ArenaRankInfos(input)

   def resume(self):
      super().resume()
      self.team.resum()
      self.duel.resum()
