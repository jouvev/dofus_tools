class GameRolePlayMonsterNotAngryAtPlayerMessage:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._monsterGroupIdFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GameRolePlayMonsterNotAngryAtPlayerMessage.playerId.")
   
   def _monsterGroupIdFunc(self,input) :
      self.monsterGroupId = input.readDouble()
      if(self.monsterGroupId < -9007199254740992 or self.monsterGroupId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.monsterGroupId) + ") on element of GameRolePlayMonsterNotAngryAtPlayerMessage.monsterGroupId.")

   def resume(self):
      print("playerId :",self.playerId)
      print("monsterGroupId :",self.monsterGroupId)
