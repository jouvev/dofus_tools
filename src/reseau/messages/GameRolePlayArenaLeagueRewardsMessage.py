class GameRolePlayArenaLeagueRewardsMessage:
   def __init__(self,input):
      self._seasonIdFunc(input)
      self._leagueIdFunc(input)
      self._ladderPositionFunc(input)
      self._endSeasonRewardFunc(input)
   
   def _seasonIdFunc(self,input) :
      self.seasonId = input.readVarUhShort()
      if(self.seasonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.seasonId) + ") on element of GameRolePlayArenaLeagueRewardsMessage.seasonId.")
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarUhShort()
      if(self.leagueId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.leagueId) + ") on element of GameRolePlayArenaLeagueRewardsMessage.leagueId.")
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()
   
   def _endSeasonRewardFunc(self,input) :
      self.endSeasonReward = input.readBoolean()

   def resume(self):
      print("seasonId :",self.seasonId)
      print("leagueId :",self.leagueId)
      print("ladderPosition :",self.ladderPosition)
      print("endSeasonReward :",self.endSeasonReward)
