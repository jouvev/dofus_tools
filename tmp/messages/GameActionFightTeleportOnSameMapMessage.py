from tmp.messages.AbstractGameActionMessage import AbstractGameActionMessage

class GameActionFightTeleportOnSameMapMessage(AbstractGameActionMessage):
   def __init__(self,input):
      super().__init__(input)
      self._targetIdFunc(input)
      self._cellIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of GameActionFightTeleportOnSameMapMessage.targetId.")
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readShort()
      if(self.cellId < -1 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of GameActionFightTeleportOnSameMapMessage.cellId.")

   def resume(self):
      super().resume()
      print("targetId :",self.targetId)
      print("cellId :",self.cellId)
