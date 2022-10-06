class GameRolePlayArenaFightPropositionMessage:
   def __init__(self,input):
      self.alliesId = []
      _val2 = None
      self._fightIdFunc(input)
      _alliesIdLen = input.readUnsignedShort()
      for _i2 in range(0,_alliesIdLen):
         _val2 = input.readDouble()
         if(_val2 < -9007199254740992 or _val2 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of alliesId.")
         self.alliesId.append(_val2)
      self._durationFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameRolePlayArenaFightPropositionMessage.fightId.")
   
   def _durationFunc(self,input) :
      self.duration = input.readVarUhShort()
      if(self.duration < 0) :
         raise RuntimeError("Forbidden value (" + str(self.duration) + ") on element of GameRolePlayArenaFightPropositionMessage.duration.")

   def resume(self):
      print("fightId :",self.fightId)
      print("duration :",self.duration)
      print("alliesId :",self.alliesId)
