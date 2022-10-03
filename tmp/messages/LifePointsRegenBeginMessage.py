class LifePointsRegenBeginMessage:
   def __init__(self,input):
      self._regenRateFunc(input)
   
   def _regenRateFunc(self,input) :
      self.regenRate = input.readUnsignedByte()
      if(self.regenRate < 0 or self.regenRate > 255) :
         raise RuntimeError("Forbidden value (" + self.regenRate + ") on element of LifePointsRegenBeginMessage.regenRate.")