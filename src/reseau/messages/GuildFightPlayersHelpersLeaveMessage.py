class GuildFightPlayersHelpersLeaveMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._playerIdFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readDouble()
      if(self.fightId < 0 or self.fightId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GuildFightPlayersHelpersLeaveMessage.fightId.")
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GuildFightPlayersHelpersLeaveMessage.playerId.")

   def resume(self):
      print("fightId :",self.fightId)
      print("playerId :",self.playerId)
