class GameFightRemoveTeamMemberMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._teamIdFunc(input)
      self._charIdFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + self.fightId + ") on element of GameFightRemoveTeamMemberMessage.fightId.")
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + self.teamId + ") on element of GameFightRemoveTeamMemberMessage.teamId.")
   
   def _charIdFunc(self,input) :
      self.charId = input.readDouble()
      if(self.charId < -9007199254740992 or self.charId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.charId + ") on element of GameFightRemoveTeamMemberMessage.charId.")