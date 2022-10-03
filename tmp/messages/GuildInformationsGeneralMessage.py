class GuildInformationsGeneralMessage:
   def __init__(self,input):
      self._abandonnedPaddockFunc(input)
      self._levelFunc(input)
      self._expLevelFloorFunc(input)
      self._experienceFunc(input)
      self._expNextLevelFloorFunc(input)
      self._creationDateFunc(input)
      self._nbTotalMembersFunc(input)
      self._nbConnectedMembersFunc(input)
   
   def _abandonnedPaddockFunc(self,input) :
      self.abandonnedPaddock = input.readBoolean()
   
   def _levelFunc(self,input) :
      self.level = input.readUnsignedByte()
      if(self.level < 0 or self.level > 255) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of GuildInformationsGeneralMessage.level.")
   
   def _expLevelFloorFunc(self,input) :
      self.expLevelFloor = input.readVarUhLong()
      if(self.expLevelFloor < 0 or self.expLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.expLevelFloor + ") on element of GuildInformationsGeneralMessage.expLevelFloor.")
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experience + ") on element of GuildInformationsGeneralMessage.experience.")
   
   def _expNextLevelFloorFunc(self,input) :
      self.expNextLevelFloor = input.readVarUhLong()
      if(self.expNextLevelFloor < 0 or self.expNextLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.expNextLevelFloor + ") on element of GuildInformationsGeneralMessage.expNextLevelFloor.")
   
   def _creationDateFunc(self,input) :
      self.creationDate = input.readInt()
      if(self.creationDate < 0) :
         raise RuntimeError("Forbidden value (" + self.creationDate + ") on element of GuildInformationsGeneralMessage.creationDate.")
   
   def _nbTotalMembersFunc(self,input) :
      self.nbTotalMembers = input.readVarUhShort()
      if(self.nbTotalMembers < 0) :
         raise RuntimeError("Forbidden value (" + self.nbTotalMembers + ") on element of GuildInformationsGeneralMessage.nbTotalMembers.")
   
   def _nbConnectedMembersFunc(self,input) :
      self.nbConnectedMembers = input.readVarUhShort()
      if(self.nbConnectedMembers < 0) :
         raise RuntimeError("Forbidden value (" + self.nbConnectedMembers + ") on element of GuildInformationsGeneralMessage.nbConnectedMembers.")