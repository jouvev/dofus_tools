class ArenaLeagueRanking:
   def __init__(self,input):
      self._rankFunc(input)
      self._leagueIdFunc(input)
      self._leaguePointsFunc(input)
      self._totalLeaguePointsFunc(input)
      self._ladderPositionFunc(input)
   
   def _rankFunc(self,input) :
      self.rank = input.readVarUhShort()
      if(self.rank < 0 or self.rank > 20000) :
         raise RuntimeError("Forbidden value (" + str(self.rank) + ") on element of ArenaLeagueRanking.rank.")
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarUhShort()
      if(self.leagueId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.leagueId) + ") on element of ArenaLeagueRanking.leagueId.")
   
   def _leaguePointsFunc(self,input) :
      self.leaguePoints = input.readVarShort()
   
   def _totalLeaguePointsFunc(self,input) :
      self.totalLeaguePoints = input.readVarShort()
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()

   def resume(self):
      print("rank :",self.rank)
      print("leagueId :",self.leagueId)
      print("leaguePoints :",self.leaguePoints)
      print("totalLeaguePoints :",self.totalLeaguePoints)
      print("ladderPosition :",self.ladderPosition)
