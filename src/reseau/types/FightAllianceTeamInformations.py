from src.reseau.types.FightTeamInformations import FightTeamInformations

class FightAllianceTeamInformations(FightTeamInformations):
   def __init__(self,input):
      super().__init__(input)
      self._relationFunc(input)
   
   def _relationFunc(self,input) :
      self.relation = input.readByte()
      if(self.relation < 0) :
         raise RuntimeError("Forbidden value (" + str(self.relation) + ") on element of FightAllianceTeamInformations.relation.")

   def resume(self):
      super().resume()
      print("relation :",self.relation)
