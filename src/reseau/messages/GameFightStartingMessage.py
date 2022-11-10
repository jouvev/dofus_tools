class GameFightStartingMessage:
   def __init__(self,input):
      self.monsters = []
      _val6 = 0
      self._fightTypeFunc(input)
      self._fightIdFunc(input)
      self._attackerIdFunc(input)
      self._defenderIdFunc(input)
      self._containsBossFunc(input)
      _monstersLen = input.readUnsignedShort()
      for _i6 in range(0,_monstersLen):
         _val6 = input.readInt()
         self.monsters.append(_val6)
   
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
   
   def _defenderIdFunc(self,input) :
      self.defenderId = input.readDouble()
      if(self.defenderId < -9007199254740992 or self.defenderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.defenderId) + ") on element of GameFightStartingMessage.defenderId.")
   
   def _containsBossFunc(self,input) :
      self.containsBoss = input.readBoolean()

   def resume(self):
      print("fightType :",self.fightType)
      print("fightId :",self.fightId)
      print("attackerId :",self.attackerId)
      print("defenderId :",self.defenderId)
      print("containsBoss :",self.containsBoss)
      print("monsters :",self.monsters)
