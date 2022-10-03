class GuildApplicationAnswerMessage:
   def __init__(self,input):
      self._acceptedFunc(input)
      self._playerIdFunc(input)
   
   def _acceptedFunc(self,input) :
      self.accepted = input.readBoolean()
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of GuildApplicationAnswerMessage.playerId.")