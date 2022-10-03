from tmp.types.BasicGuildInformations import BasicGuildInformations
from tmp.types.FightResultFighterListEntry import FightResultFighterListEntry
class FightResultTaxCollectorListEntry(FightResultFighterListEntry):
   def __init__(self,input):
      super().__init__(input)
      self._levelFunc(input)
      self.guildInfo = BasicGuildInformations(input)
      self._experienceForGuildFunc(input)
   
   def _levelFunc(self,input) :
      self.level = input.readUnsignedByte()
      if(self.level < 1 or self.level > 200) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of FightResultTaxCollectorListEntry.level.")
   
   def _experienceForGuildFunc(self,input) :
      self.experienceForGuild = input.readInt()