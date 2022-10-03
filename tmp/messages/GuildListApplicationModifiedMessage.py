from tmp.types.GuildApplicationInformation import GuildApplicationInformation
class GuildListApplicationModifiedMessage:
   def __init__(self,input):
      self.apply = GuildApplicationInformation(input)
      self._stateFunc(input)
      self._playerIdFunc(input)
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of GuildListApplicationModifiedMessage.state.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of GuildListApplicationModifiedMessage.playerId.")