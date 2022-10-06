class GameRolePlayAggressionMessage:
   def __init__(self,input):
      self._attackerIdFunc(input)
   def _attackerIdFunc(self,input) :
      self.attackerId = input.readVarUhLong()
      if(self.attackerId < 0 or self.attackerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.attackerId) + ") on element of GameRolePlayAggressionMessage.attackerId.")

   def resume(self):
      print("attackerId :",self.attackerId)
