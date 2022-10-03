from tmp.types.PartyMemberInformations import PartyMemberInformations
class PartyMemberArenaInformations(PartyMemberInformations):
   def __init__(self,input):
      super().__init__(input)
      self._rankFunc(input)
   
   def _rankFunc(self,input) :
      self.rank = input.readVarUhShort()
      if(self.rank < 0 or self.rank > 20000) :
         raise RuntimeError("Forbidden value (" + self.rank + ") on element of PartyMemberArenaInformations.rank.")