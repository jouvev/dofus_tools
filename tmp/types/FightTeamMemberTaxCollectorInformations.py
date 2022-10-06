from tmp.types.FightTeamMemberInformations import FightTeamMemberInformations

class FightTeamMemberTaxCollectorInformations(FightTeamMemberInformations):
   def __init__(self,input):
      super().__init__(input)
      self._firstNameIdFunc(input)
      self._lastNameIdFunc(input)
      self._levelFunc(input)
      self._guildIdFunc(input)
      self._uidFunc(input)
   
   def _firstNameIdFunc(self,input) :
      self.firstNameId = input.readVarUhShort()
      if(self.firstNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.firstNameId) + ") on element of FightTeamMemberTaxCollectorInformations.firstNameId.")
   
   def _lastNameIdFunc(self,input) :
      self.lastNameId = input.readVarUhShort()
      if(self.lastNameId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastNameId) + ") on element of FightTeamMemberTaxCollectorInformations.lastNameId.")
   
   def _levelFunc(self,input) :
      self.level = input.readUnsignedByte()
      if(self.level < 1 or self.level > 200) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of FightTeamMemberTaxCollectorInformations.level.")
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of FightTeamMemberTaxCollectorInformations.guildId.")
   
   def _uidFunc(self,input) :
      self.uid = input.readDouble()
      if(self.uid < 0 or self.uid > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.uid) + ") on element of FightTeamMemberTaxCollectorInformations.uid.")

   def resume(self):
      super().resume()
      print("firstNameId :",self.firstNameId)
      print("lastNameId :",self.lastNameId)
      print("level :",self.level)
      print("guildId :",self.guildId)
      print("uid :",self.uid)
