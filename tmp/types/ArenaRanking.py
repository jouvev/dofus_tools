class ArenaRanking:
   def __init__(self,input):
      self._rankFunc(input)
      self._bestRankFunc(input)
   
   def _rankFunc(self,input) :
      self.rank = input.readVarUhShort()
      if(self.rank < 0 or self.rank > 20000) :
         raise RuntimeError("Forbidden value (" + self.rank + ") on element of ArenaRanking.rank.")
   
   def _bestRankFunc(self,input) :
      self.bestRank = input.readVarUhShort()
      if(self.bestRank < 0 or self.bestRank > 20000) :
         raise RuntimeError("Forbidden value (" + self.bestRank + ") on element of ArenaRanking.bestRank.")