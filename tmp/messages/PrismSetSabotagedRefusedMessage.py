class PrismSetSabotagedRefusedMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._reasonFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismSetSabotagedRefusedMessage.subAreaId.")
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()