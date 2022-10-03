from tmp.types.GuildRankMinimalInformation import GuildRankMinimalInformation
from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
class GuildPlayerRankUpdateActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self.guildRankMinimalInfos = GuildRankMinimalInformation(input)
      self._sourcePlayerIdFunc(input)
      self._targetPlayerIdFunc(input)
      self._sourcePlayerNameFunc(input)
      self._targetPlayerNameFunc(input)
   
   def _sourcePlayerIdFunc(self,input) :
      self.sourcePlayerId = input.readVarUhLong()
      if(self.sourcePlayerId < 0 or self.sourcePlayerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.sourcePlayerId + ") on element of GuildPlayerRankUpdateActivity.sourcePlayerId.")
   
   def _targetPlayerIdFunc(self,input) :
      self.targetPlayerId = input.readVarUhLong()
      if(self.targetPlayerId < 0 or self.targetPlayerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetPlayerId + ") on element of GuildPlayerRankUpdateActivity.targetPlayerId.")
   
   def _sourcePlayerNameFunc(self,input) :
      self.sourcePlayerName = input.readUTF()
   
   def _targetPlayerNameFunc(self,input) :
      self.targetPlayerName = input.readUTF()