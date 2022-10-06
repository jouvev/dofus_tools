class GameRolePlayFightRequestCanceledMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self._sourceIdFunc(input)
      self._targetIdFunc(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readVarUhShort()
      if(self.fightId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GameRolePlayFightRequestCanceledMessage.fightId.")
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readDouble()
      if(self.sourceId < -9007199254740992 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sourceId) + ") on element of GameRolePlayFightRequestCanceledMessage.sourceId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameRolePlayFightRequestCanceledMessage.targetId.")

   def resume(self):
      print("fightId :",self.fightId)
      print("sourceId :",self.sourceId)
      print("targetId :",self.targetId)
