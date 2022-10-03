class GameRolePlayPlayerFightRequestMessage:
   def __init__(self,input):
      self._targetIdFunc(input)
      self._targetCellIdFunc(input)
      self._friendlyFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readVarUhLong()
      if(self.targetId < 0 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GameRolePlayPlayerFightRequestMessage.targetId.")
   
   def _targetCellIdFunc(self,input) :
      self.targetCellId = input.readShort()
      if(self.targetCellId < -1 or self.targetCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.targetCellId + ") on element of GameRolePlayPlayerFightRequestMessage.targetCellId.")
   
   def _friendlyFunc(self,input) :
      self.friendly = input.readBoolean()