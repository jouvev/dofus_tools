from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation

class GuildLevelUpActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._newGuildLevelFunc(input)
   
   def _newGuildLevelFunc(self,input) :
      self.newGuildLevel = input.readUnsignedByte()
      if(self.newGuildLevel < 0 or self.newGuildLevel > 255) :
         raise RuntimeError("Forbidden value (" + str(self.newGuildLevel) + ") on element of GuildLevelUpActivity.newGuildLevel.")

   def resume(self):
      super().resume()
      print("newGuildLevel :",self.newGuildLevel)
