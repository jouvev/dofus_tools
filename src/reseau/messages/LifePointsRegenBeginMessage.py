class LifePointsRegenBeginMessage:
   def __init__(self,input):
      self._regenRateFunc(input)
   
   def _regenRateFunc(self,input) :
      self.regenRate = input.readUnsignedByte()
      if(self.regenRate < 0 or self.regenRate > 255) :
         raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element of LifePointsRegenBeginMessage.regenRate.")

   def resume(self):
      print("regenRate :",self.regenRate)
