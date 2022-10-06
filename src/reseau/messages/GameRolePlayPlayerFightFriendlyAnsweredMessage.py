class GameRolePlayPlayerFightFriendlyAnsweredMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._sourceIdFunc(input)
      self._targetIdFunc(input)
      self._acceptFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameRolePlayPlayerFightFriendlyAnsweredMessage.fightId.")
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readVarUhLong()
      if(self.sourceId < 0 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sourceId) + ") on element of GameRolePlayPlayerFightFriendlyAnsweredMessage.sourceId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readVarUhLong()
      if(self.targetId < 0 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameRolePlayPlayerFightFriendlyAnsweredMessage.targetId.")
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()

   def resume(self):
      print("fightId :",self.fightId)
      print("sourceId :",self.sourceId)
      print("targetId :",self.targetId)
      print("accept :",self.accept)
