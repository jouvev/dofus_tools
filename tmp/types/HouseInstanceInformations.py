from tmp.types.AccountTagInformation import AccountTagInformation

class HouseInstanceInformations:
   def __init__(self,input):
      self.deserializeByteBoxes(input)
      self._instanceIdFunc(input)
      self.ownerTag = AccountTagInformation(input)
      self._priceFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.secondHand = bool(bin(_box0)[2:].zfill(8)[0])
      self.isLocked = bool(bin(_box0)[2:].zfill(8)[1])
      self.hasOwner = bool(bin(_box0)[2:].zfill(8)[2])
      self.isSaleLocked = bool(bin(_box0)[2:].zfill(8)[3])
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseInstanceInformations.instanceId.")
   
   def _priceFunc(self,input) :
      self.price = input.readVarLong()
      if(self.price < -9007199254740992 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of HouseInstanceInformations.price.")

   def resume(self):
      print("instanceId :",self.instanceId)
      print("price :",self.price)
      self.ownerTag.resum()
