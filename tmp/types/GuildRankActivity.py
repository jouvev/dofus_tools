from tmp.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
class GuildRankActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._rankActivityTypeFunc(input)
      self.guildRankMinimalInfos = GuildRankMinimalInformation(input)
   
   def _rankActivityTypeFunc(self,input) :
      self.rankActivityType = input.readByte()
      if(self.rankActivityType < 0) :
         raise RuntimeError("Forbidden value (" + self.rankActivityType + ") on element of GuildRankActivity.rankActivityType.")