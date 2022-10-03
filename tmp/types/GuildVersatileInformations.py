class GuildVersatileInformations:
   def __init__(self,input):
      self._guildIdFunc(input)
      self._leaderIdFunc(input)
      self._guildLevelFunc(input)
      self._nbMembersFunc(input)
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + self.guildId + ") on element of GuildVersatileInformations.guildId.")
   
   def _leaderIdFunc(self,input) :
      self.leaderId = input.readVarUhLong()
      if(self.leaderId < 0 or self.leaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.leaderId + ") on element of GuildVersatileInformations.leaderId.")
   
   def _guildLevelFunc(self,input) :
      self.guildLevel = input.readUnsignedByte()
      if(self.guildLevel < 1 or self.guildLevel > 200) :
         raise RuntimeError("Forbidden value (" + self.guildLevel + ") on element of GuildVersatileInformations.guildLevel.")
   
   def _nbMembersFunc(self,input) :
      self.nbMembers = input.readUnsignedByte()
      if(self.nbMembers < 1 or self.nbMembers > 240) :
         raise RuntimeError("Forbidden value (" + self.nbMembers + ") on element of GuildVersatileInformations.nbMembers.")