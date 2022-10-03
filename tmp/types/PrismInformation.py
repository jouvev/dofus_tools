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
         raise RuntimeError("Forbidden value (" + self.typeId + ") on element of PrismInformation.typeId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of PrismInformation.state.")
   
   def _nextVulnerabilityDateFunc(self,input) :
      self.nextVulnerabilityDate = input.readInt()
      if(self.nextVulnerabilityDate < 0) :
         raise RuntimeError("Forbidden value (" + self.nextVulnerabilityDate + ") on element of PrismInformation.nextVulnerabilityDate.")
   
   def _placementDateFunc(self,input) :
      self.placementDate = input.readInt()
      if(self.placementDate < 0) :
         raise RuntimeError("Forbidden value (" + self.placementDate + ") on element of PrismInformation.placementDate.")
   
   def _rewardTokenCountFunc(self,input) :
      self.rewardTokenCount = input.readVarUhInt()
      if(self.rewardTokenCount < 0) :
         raise RuntimeError("Forbidden value (" + self.rewardTokenCount + ") on element of PrismInformation.rewardTokenCount.")