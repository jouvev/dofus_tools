class GuildFactsErrorMessage:
   def __init__(self,input):
      self._guildIdFunc(input)
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of GuildFactsErrorMessage.guildId.")

   def resume(self):
      print("guildId :",self.guildId)
