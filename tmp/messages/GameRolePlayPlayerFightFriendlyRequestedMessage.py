class GameRolePlayPlayerFightFriendlyRequestedMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._sourceIdFunc(input)
      self._targetIdFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + self.fightId + ") on element of GameRolePlayPlayerFightFriendlyRequestedMessage.fightId.")
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readVarUhLong()
      if(self.sourceId < 0 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.sourceId + ") on element of GameRolePlayPlayerFightFriendlyRequestedMessage.sourceId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readVarUhLong()
      if(self.targetId < 0 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GameRolePlayPlayerFightFriendlyRequestedMessage.targetId.")