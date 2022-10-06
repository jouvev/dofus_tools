class GameFightStartingMessage:
   def __init__(self,input):
      _val6 = 0
      self._fightTypeFunc(input)
      self._fightIdFunc(input)
      self._attackerIdFunc(input)
   def _fightTypeFunc(self,input) :
      self.fightType = input.readByte()
      if(self.fightType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightType) + ") on element of GameFightStartingMessage.fightType.")
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameFightStartingMessage.fightId.")
   
   def _attackerIdFunc(self,input) :
      self.attackerId = input.readDouble()
      if(self.attackerId < -9007199254740992 or self.attackerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.attackerId) + ") on element of GameFightStartingMessage.attackerId.")

   def resume(self):
      print("fightType :",self.fightType)
      print("fightId :",self.fightId)
      print("attackerId :",self.attackerId)
