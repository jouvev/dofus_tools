from src.reseau.types.GuildInformations import GuildInformations

class GuildJoinedMessage:
   def __init__(self,input):
      self.guildInfo = GuildInformations(input)
      self._rankIdFunc(input)
   
   def _rankIdFunc(self,input) :
      self.rankId = input.readVarUhInt()
      if(self.rankId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rankId) + ") on element of GuildJoinedMessage.rankId.")

   def resume(self):
      print("rankId :",self.rankId)
      self.guildInfo.resum()
