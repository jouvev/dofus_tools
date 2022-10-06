class AllianceChangeGuildRightsMessage:
   def __init__(self,input):
      self._guildIdFunc(input)
      self._rightsFunc(input)
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of AllianceChangeGuildRightsMessage.guildId.")
   
   def _rightsFunc(self,input) :
      self.rights = input.readByte()
      if(self.rights < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rights) + ") on element of AllianceChangeGuildRightsMessage.rights.")

   def resume(self):
      print("guildId :",self.guildId)
      print("rights :",self.rights)
