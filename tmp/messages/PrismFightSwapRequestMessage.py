class PrismFightSwapRequestMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._targetIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismFightSwapRequestMessage.subAreaId.")
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readVarUhLong()
      if(self.targetId < 0 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of PrismFightSwapRequestMessage.targetId.")