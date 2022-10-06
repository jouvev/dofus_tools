from tmp.types.NamedPartyTeam import NamedPartyTeam

class NamedPartyTeamWithOutcome:
   def __init__(self,input):
      self.team = NamedPartyTeam(input)
      self._outcomeFunc(input)
   
   def _outcomeFunc(self,input) :
      self.outcome = input.readVarUhShort()
      if(self.outcome < 0) :
         raise RuntimeError("Forbidden value (" + str(self.outcome) + ") on element of NamedPartyTeamWithOutcome.outcome.")

   def resume(self):
      print("outcome :",self.outcome)
      self.team.resum()
