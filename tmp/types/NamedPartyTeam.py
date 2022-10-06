class NamedPartyTeam:
   def __init__(self,input):
      self._teamIdFunc(input)
      self._partyNameFunc(input)
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.teamId) + ") on element of NamedPartyTeam.teamId.")
   
   def _partyNameFunc(self,input) :
      self.partyName = input.readUTF()

   def resume(self):
      print("teamId :",self.teamId)
      print("partyName :",self.partyName)
