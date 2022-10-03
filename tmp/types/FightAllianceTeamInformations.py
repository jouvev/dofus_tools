from tmp.types.FightTeamInformations import FightTeamInformations
class FightAllianceTeamInformations(FightTeamInformations):
   def __init__(self,input):
      super().__init__(input)
      self._relationFunc(input)
   
   def _relationFunc(self,input) :
      self.relation = input.readByte()
      if(self.relation < 0) :
         raise RuntimeError("Forbidden value (" + self.relation + ") on element of FightAllianceTeamInformations.relation.")