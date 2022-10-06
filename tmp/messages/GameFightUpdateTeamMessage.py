from tmp.types.FightTeamInformations import FightTeamInformations

class GameFightUpdateTeamMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self.team = FightTeamInformations(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameFightUpdateTeamMessage.fightId.")

   def resume(self):
      print("fightId :",self.fightId)
      self.team.resum()
