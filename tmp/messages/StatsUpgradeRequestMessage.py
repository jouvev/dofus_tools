class StatsUpgradeRequestMessage:
   def __init__(self,input):
      self._useAdditionnalFunc(input)
      self._statIdFunc(input)
      self._boostPointFunc(input)
   
   def _useAdditionnalFunc(self,input) :
      self.useAdditionnal = input.readBoolean()
   
   def _statIdFunc(self,input) :
      self.statId = input.readByte()
      if(self.statId < 0) :
         raise RuntimeError("Forbidden value (" + self.statId + ") on element of StatsUpgradeRequestMessage.statId.")
   
   def _boostPointFunc(self,input) :
      self.boostPoint = input.readVarUhShort()
      if(self.boostPoint < 0) :
         raise RuntimeError("Forbidden value (" + self.boostPoint + ") on element of StatsUpgradeRequestMessage.boostPoint.")