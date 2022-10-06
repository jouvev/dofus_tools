from tmp.types.HumanOption import HumanOption

class HumanOptionObjectUse(HumanOption):
   def __init__(self,input):
      super().__init__(input)
      self._delayTypeIdFunc(input)
      self._delayEndTimeFunc(input)
      self._objectGIDFunc(input)
   
   def _delayTypeIdFunc(self,input) :
      self.delayTypeId = input.readByte()
      if(self.delayTypeId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.delayTypeId) + ") on element of HumanOptionObjectUse.delayTypeId.")
   
   def _delayEndTimeFunc(self,input) :
      self.delayEndTime = input.readDouble()
      if(self.delayEndTime < 0 or self.delayEndTime > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.delayEndTime) + ") on element of HumanOptionObjectUse.delayEndTime.")
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGID) + ") on element of HumanOptionObjectUse.objectGID.")

   def resume(self):
      super().resume()
      print("delayTypeId :",self.delayTypeId)
      print("delayEndTime :",self.delayEndTime)
      print("objectGID :",self.objectGID)
