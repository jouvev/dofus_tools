from src.reseau.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from src.reseau.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation

class GuildRankActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._rankActivityTypeFunc(input)
      self.guildRankMinimalInfos = GuildRankMinimalInformation(input)
   
   def _rankActivityTypeFunc(self,input) :
      self.rankActivityType = input.readByte()
      if(self.rankActivityType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rankActivityType) + ") on element of GuildRankActivity.rankActivityType.")

   def resume(self):
      super().resume()
      print("rankActivityType :",self.rankActivityType)
      self.guildRankMinimalInfos.resum()
