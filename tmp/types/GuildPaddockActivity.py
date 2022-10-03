from tmp.types.MapCoordinatesExtended import MapCoordinatesExtended
from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation
class GuildPaddockActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self.paddockCoordinates = MapCoordinatesExtended(input)
      self._farmIdFunc(input)
      self._paddockEventTypeFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of GuildPaddockActivity.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _farmIdFunc(self,input) :
      self.farmId = input.readDouble()
      if(self.farmId < 0 or self.farmId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.farmId + ") on element of GuildPaddockActivity.farmId.")
   
   def _paddockEventTypeFunc(self,input) :
      self.paddockEventType = input.readByte()
      if(self.paddockEventType < 0) :
         raise RuntimeError("Forbidden value (" + self.paddockEventType + ") on element of GuildPaddockActivity.paddockEventType.")