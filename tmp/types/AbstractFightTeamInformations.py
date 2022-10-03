class AbstractFightTeamInformations:
   def __init__(self,input):
      self._teamIdFunc(input)
      self._leaderIdFunc(input)
      self._teamSideFunc(input)
      self._teamTypeIdFunc(input)
      self._nbWavesFunc(input)
   
   def _teamIdFunc(self,input) :
      self.teamId = input.readByte()
      if(self.teamId < 0) :
         raise RuntimeError("Forbidden value (" + self.teamId + ") on element of AbstractFightTeamInformations.teamId.")
   
   def _leaderIdFunc(self,input) :
      self.leaderId = input.readDouble()
      if(self.leaderId < -9007199254740992 or self.leaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.leaderId + ") on element of AbstractFightTeamInformations.leaderId.")
   
   def _teamSideFunc(self,input) :
      self.teamSide = input.readByte()
   
   def _teamTypeIdFunc(self,input) :
      self.teamTypeId = input.readByte()
      if(self.teamTypeId < 0) :
         raise RuntimeError("Forbidden value (" + self.teamTypeId + ") on element of AbstractFightTeamInformations.teamTypeId.")
   
   def _nbWavesFunc(self,input) :
      self.nbWaves = input.readByte()
      if(self.nbWaves < 0) :
         raise RuntimeError("Forbidden value (" + self.nbWaves + ") on element of AbstractFightTeamInformations.nbWaves.")