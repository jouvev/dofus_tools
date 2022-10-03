class AnomalyStateMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._openFunc(input)
      self._closingTimeFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of AnomalyStateMessage.subAreaId.")
   
   def _openFunc(self,input) :
      self.open = input.readBoolean()
   
   def _closingTimeFunc(self,input) :
      self.closingTime = input.readVarUhLong()
      if(self.closingTime < 0 or self.closingTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.closingTime + ") on element of AnomalyStateMessage.closingTime.")