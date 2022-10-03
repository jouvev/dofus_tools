class GuildLevelUpMessage:
   def __init__(self,input):
      self._newLevelFunc(input)
   
   def _newLevelFunc(self,input) :
      self.newLevel = input.readUnsignedByte()
      if(self.newLevel < 2 or self.newLevel > 200) :
         raise RuntimeError("Forbidden value (" + self.newLevel + ") on element of GuildLevelUpMessage.newLevel.")