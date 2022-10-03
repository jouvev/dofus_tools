class StatsUpgradeResultMessage:
   def __init__(self,input):
      self._resultFunc(input)
      self._nbCharacBoostFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
   
   def _nbCharacBoostFunc(self,input) :
      self.nbCharacBoost = input.readVarUhShort()
      if(self.nbCharacBoost < 0) :
         raise RuntimeError("Forbidden value (" + self.nbCharacBoost + ") on element of StatsUpgradeResultMessage.nbCharacBoost.")