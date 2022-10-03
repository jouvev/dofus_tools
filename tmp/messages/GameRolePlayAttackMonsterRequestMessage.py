class GameRolePlayAttackMonsterRequestMessage:
   def __init__(self,input):
      self._monsterGroupIdFunc(input)
   
   def _monsterGroupIdFunc(self,input) :
      self.monsterGroupId = input.readDouble()
      if(self.monsterGroupId < -9007199254740992 or self.monsterGroupId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.monsterGroupId + ") on element of GameRolePlayAttackMonsterRequestMessage.monsterGroupId.")