class GuildApplicationReceivedMessage:
   def __init__(self,input):
      self._playerNameFunc(input)
      self._playerIdFunc(input)
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of GuildApplicationReceivedMessage.playerId.")