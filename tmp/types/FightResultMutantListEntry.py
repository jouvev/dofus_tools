from tmp.types.FightResultFighterListEntry import FightResultFighterListEntry
class FightResultMutantListEntry(FightResultFighterListEntry):
   def __init__(self,input):
      super().__init__(input)
      self._levelFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of FightResultMutantListEntry.level.")