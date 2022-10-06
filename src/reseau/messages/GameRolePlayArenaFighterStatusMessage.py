class GameRolePlayArenaFighterStatusMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._playerIdFunc(input)
      self._acceptedFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameRolePlayArenaFighterStatusMessage.fightId.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GameRolePlayArenaFighterStatusMessage.playerId.")
   
   def _acceptedFunc(self,input) :
      self.accepted = input.readBoolean()

   def resume(self):
      print("fightId :",self.fightId)
      print("playerId :",self.playerId)
      print("accepted :",self.accepted)
