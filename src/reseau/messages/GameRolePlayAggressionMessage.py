class GameRolePlayAggressionMessage:
   def __init__(self,input):
      self._attackerIdFunc(input)
      self._defenderIdFunc(input)
   
   def _attackerIdFunc(self,input) :
      self.attackerId = input.readVarUhLong()
      if(self.attackerId < 0 or self.attackerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.attackerId) + ") on element of GameRolePlayAggressionMessage.attackerId.")
   
   def _defenderIdFunc(self,input) :
      self.defenderId = input.readVarUhLong()
      if(self.defenderId < 0 or self.defenderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.defenderId) + ") on element of GameRolePlayAggressionMessage.defenderId.")

   def resume(self):
      print("attackerId :",self.attackerId)
      print("defenderId :",self.defenderId)
