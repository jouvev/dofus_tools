from tmp.types.ArenaRanking import ArenaRanking
from tmp.types.ArenaLeagueRanking import ArenaLeagueRanking
class ArenaRankInfos:
   def __init__(self,input):
      if(input.readByte() == 0) :
         self.ranking = None
      else :
         self.ranking = ArenaRanking(input)
      if(input.readByte() == 0) :
         self.leagueRanking = None
      else :
         self.leagueRanking = ArenaLeagueRanking(input)
      self._victoryCountFunc(input)
      self._fightcountFunc(input)
      self._numFightNeededForLadderFunc(input)
   
   def _victoryCountFunc(self,input) :
      self.victoryCount = input.readVarUhShort()
      if(self.victoryCount < 0) :
         raise RuntimeError("Forbidden value (" + self.victoryCount + ") on element of ArenaRankInfos.victoryCount.")
   
   def _fightcountFunc(self,input) :
      self.fightcount = input.readVarUhShort()
      if(self.fightcount < 0) :
         raise RuntimeError("Forbidden value (" + self.fightcount + ") on element of ArenaRankInfos.fightcount.")
   
   def _numFightNeededForLadderFunc(self,input) :
      self.numFightNeededForLadder = input.readShort()
      if(self.numFightNeededForLadder < 0) :
         raise RuntimeError("Forbidden value (" + self.numFightNeededForLadder + ") on element of ArenaRankInfos.numFightNeededForLadder.")