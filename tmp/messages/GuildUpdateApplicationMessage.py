class GuildUpdateApplicationMessage:
   def __init__(self,input):
      self._applyTextFunc(input)
      self._guildIdFunc(input)
   
   def _applyTextFunc(self,input) :
      self.applyText = input.readUTF()
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + self.guildId + ") on element of GuildUpdateApplicationMessage.guildId.")