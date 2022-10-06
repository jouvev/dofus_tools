from src.reseau.types.AbstractSocialGroupInfos import AbstractSocialGroupInfos

class BasicGuildInformations(AbstractSocialGroupInfos):
   def __init__(self,input):
      super().__init__(input)
      self._guildIdFunc(input)
      self._guildNameFunc(input)
      self._guildLevelFunc(input)
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of BasicGuildInformations.guildId.")
   
   def _guildNameFunc(self,input) :
      self.guildName = input.readUTF()
   
   def _guildLevelFunc(self,input) :
      self.guildLevel = input.readUnsignedByte()
      if(self.guildLevel < 0 or self.guildLevel > 200) :
         raise RuntimeError("Forbidden value (" + str(self.guildLevel) + ") on element of BasicGuildInformations.guildLevel.")

   def resume(self):
      super().resume()
      print("guildId :",self.guildId)
      print("guildName :",self.guildName)
      print("guildLevel :",self.guildLevel)
