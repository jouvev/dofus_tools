class PrismSubareaEmptyInfo:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._allianceIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PrismSubareaEmptyInfo.subAreaId.")
   
   def _allianceIdFunc(self,input) :
      self.allianceId = input.readVarUhInt()
      if(self.allianceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.allianceId) + ") on element of PrismSubareaEmptyInfo.allianceId.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("allianceId :",self.allianceId)
