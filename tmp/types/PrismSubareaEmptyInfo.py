class PrismSubareaEmptyInfo:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._allianceIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PrismSubareaEmptyInfo.subAreaId.")
   
   def _allianceIdFunc(self,input) :
      self.allianceId = input.readVarUhInt()
      if(self.allianceId < 0) :
         raise RuntimeError("Forbidden value (" + self.allianceId + ") on element of PrismSubareaEmptyInfo.allianceId.")