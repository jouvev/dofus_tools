class GameRolePlayMonsterAngryAtPlayerMessage:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._monsterGroupIdFunc(input)
      self._angryStartTimeFunc(input)
      self._attackTimeFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.playerId.")
   
   def _monsterGroupIdFunc(self,input) :
      self.monsterGroupId = input.readDouble()
      if(self.monsterGroupId < -9007199254740992 or self.monsterGroupId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.monsterGroupId + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.monsterGroupId.")
   
   def _angryStartTimeFunc(self,input) :
      self.angryStartTime = input.readDouble()
      if(self.angryStartTime < 0 or self.angryStartTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.angryStartTime + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.angryStartTime.")
   
   def _attackTimeFunc(self,input) :
      self.attackTime = input.readDouble()
      if(self.attackTime < 0 or self.attackTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.attackTime + ") on element of GameRolePlayMonsterAngryAtPlayerMessage.attackTime.")