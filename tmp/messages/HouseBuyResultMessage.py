class HouseBuyResultMessage:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._realPriceFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.secondHand = bool(bin(_box0)[2:].zfill(8)[0])
      self.bought = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + self.houseId + ") on element of HouseBuyResultMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + self.instanceId + ") on element of HouseBuyResultMessage.instanceId.")
   
   def _realPriceFunc(self,input) :
      self.realPrice = input.readVarUhLong()
      if(self.realPrice < 0 or self.realPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.realPrice + ") on element of HouseBuyResultMessage.realPrice.")