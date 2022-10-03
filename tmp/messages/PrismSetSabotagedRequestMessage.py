class PrismSetSabotagedRequestMessage:
   def __init__(self,input):
      self._subAreaIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismSetSabotagedRequestMessage.subAreaId.")