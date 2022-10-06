from tmp.types.ArenaRankInfos import ArenaRankInfos

class GameRolePlayArenaUpdatePlayerInfosMessage:
   def __init__(self,input):
      self.solo = ArenaRankInfos(input)

   def resume(self):
      self.solo.resum()
