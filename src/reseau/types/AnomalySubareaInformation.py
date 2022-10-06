class AnomalySubareaInformation:
   def __init__(self,input):
      self._subAreaIdFunc(input)
      self._rewardRateFunc(input)
      self._hasAnomalyFunc(input)
      self._anomalyClosingTimeFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of AnomalySubareaInformation.subAreaId.")
   
   def _rewardRateFunc(self,input) :
      self.rewardRate = input.readVarShort()
   
   def _hasAnomalyFunc(self,input) :
      self.hasAnomaly = input.readBoolean()
   
   def _anomalyClosingTimeFunc(self,input) :
      self.anomalyClosingTime = input.readVarUhLong()
      if(self.anomalyClosingTime < 0 or self.anomalyClosingTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.anomalyClosingTime) + ") on element of AnomalySubareaInformation.anomalyClosingTime.")

   def resume(self):
      print("subAreaId :",self.subAreaId)
      print("rewardRate :",self.rewardRate)
      print("hasAnomaly :",self.hasAnomaly)
      print("anomalyClosingTime :",self.anomalyClosingTime)
