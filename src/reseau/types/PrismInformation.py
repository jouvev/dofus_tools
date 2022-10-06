class PrismInformation:
   def __init__(self,input):
      self._typeIdFunc(input)
      self._stateFunc(input)
      self._nextVulnerabilityDateFunc(input)
      self._placementDateFunc(input)
      self._rewardTokenCountFunc(input)
   
   def _typeIdFunc(self,input) :
      self.typeId = input.readByte()
      if(self.typeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.typeId) + ") on element of PrismInformation.typeId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + str(self.state) + ") on element of PrismInformation.state.")
   
   def _nextVulnerabilityDateFunc(self,input) :
      self.nextVulnerabilityDate = input.readInt()
      if(self.nextVulnerabilityDate < 0) :
         raise RuntimeError("Forbidden value (" + str(self.nextVulnerabilityDate) + ") on element of PrismInformation.nextVulnerabilityDate.")
   
   def _placementDateFunc(self,input) :
      self.placementDate = input.readInt()
      if(self.placementDate < 0) :
         raise RuntimeError("Forbidden value (" + str(self.placementDate) + ") on element of PrismInformation.placementDate.")
   
   def _rewardTokenCountFunc(self,input) :
      self.rewardTokenCount = input.readVarUhInt()
      if(self.rewardTokenCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rewardTokenCount) + ") on element of PrismInformation.rewardTokenCount.")

   def resume(self):
      print("typeId :",self.typeId)
      print("state :",self.state)
      print("nextVulnerabilityDate :",self.nextVulnerabilityDate)
      print("placementDate :",self.placementDate)
      print("rewardTokenCount :",self.rewardTokenCount)
