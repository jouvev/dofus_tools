class GameRolePlayMonsterAngryAtPlayerMessage:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._monsterGroupIdFunc(input)
      self._angryStartTimeFunc(input)
      self._attackTimeFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.playerId) + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.playerId.")
   
   def _monsterGroupIdFunc(self,input) :
      self.monsterGroupId = input.readDouble()
      if(self.monsterGroupId < -9007199254740992 or self.monsterGroupId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.monsterGroupId) + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.monsterGroupId.")
   
   def _angryStartTimeFunc(self,input) :
      self.angryStartTime = input.readDouble()
      if(self.angryStartTime < 0 or self.angryStartTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.angryStartTime) + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.angryStartTime.")
   
   def _attackTimeFunc(self,input) :
      self.attackTime = input.readDouble()
      if(self.attackTime < 0 or self.attackTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.attackTime) + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.attackTime.")

   def resume(self):
      print("playerId :",self.playerId)
      print("monsterGroupId :",self.monsterGroupId)
      print("angryStartTime :",self.angryStartTime)
      print("attackTime :",self.attackTime)
