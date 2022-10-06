class TeleportOnSameMapMessage:
   def __init__(self,input):
      self._targetIdFunc(input)
      self._cellIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readDouble()
      if(self.targetId < -9007199254740992 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.targetId) + ") on element of TeleportOnSameMapMessage.targetId.")
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of TeleportOnSameMapMessage.cellId.")

   def resume(self):
      print("targetId :",self.targetId)
      print("cellId :",self.cellId)
