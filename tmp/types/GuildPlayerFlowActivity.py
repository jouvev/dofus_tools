from tmp.types.GuildLogbookEntryBasicInformation import GuildLogbookEntryBasicInformation

class GuildPlayerFlowActivity(GuildLogbookEntryBasicInformation):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._playerFlowEventTypeFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GuildPlayerFlowActivity.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _playerFlowEventTypeFunc(self,input) :
      self.playerFlowEventType = input.readByte()
      if(self.playerFlowEventType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.playerFlowEventType) + ") on element of GuildPlayerFlowActivity.playerFlowEventType.")

   def resume(self):
      super().resume()
      print("playerId :",self.playerId)
      print("playerName :",self.playerName)
      print("playerFlowEventType :",self.playerFlowEventType)
