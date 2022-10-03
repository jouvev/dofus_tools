class AllianceGuildLeavingMessage:
   def __init__(self,input):
      self._kickedFunc(input)
      self._guildIdFunc(input)
   
   def _kickedFunc(self,input) :
      self.kicked = input.readBoolean()
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + self.guildId + ") on element of AllianceGuildLeavingMessage.guildId.")