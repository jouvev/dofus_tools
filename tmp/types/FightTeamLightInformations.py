from tmp.types.AbstractFightTeamInformations import AbstractFightTeamInformations

class FightTeamLightInformations(AbstractFightTeamInformations):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._teamMembersCountFunc(input)
      self._meanLevelFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.hasFriend = bool(bin(_box0)[2:].zfill(8)[0])
      self.hasGuildMember = bool(bin(_box0)[2:].zfill(8)[1])
      self.hasAllianceMember = bool(bin(_box0)[2:].zfill(8)[2])
      self.hasGroupMember = bool(bin(_box0)[2:].zfill(8)[3])
      self.hasMyTaxCollector = bool(bin(_box0)[2:].zfill(8)[4])
   
   def _teamMembersCountFunc(self,input) :
      self.teamMembersCount = input.readByte()
      if(self.teamMembersCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.teamMembersCount) + ") on element of FightTeamLightInformations.teamMembersCount.")
   
   def _meanLevelFunc(self,input) :
      self.meanLevel = input.readVarUhInt()
      if(self.meanLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.meanLevel) + ") on element of FightTeamLightInformations.meanLevel.")

   def resume(self):
      super().resume()
      print("teamMembersCount :",self.teamMembersCount)
      print("meanLevel :",self.meanLevel)
