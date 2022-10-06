class ChallengeFightJoinRefusedMessage:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._reasonFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of ChallengeFightJoinRefusedMessage.playerId.")
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()

   def resume(self):
      print("playerId :",self.playerId)
      print("reason :",self.reason)
