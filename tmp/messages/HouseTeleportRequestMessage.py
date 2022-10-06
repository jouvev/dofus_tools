class HouseTeleportRequestMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._houseInstanceIdFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HouseTeleportRequestMessage.houseId.")
   
   def _houseInstanceIdFunc(self,input) :
      self.houseInstanceId = input.readInt()
      if(self.houseInstanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseInstanceId) + ") on element of HouseTeleportRequestMessage.houseInstanceId.")

   def resume(self):
      print("houseId :",self.houseId)
      print("houseInstanceId :",self.houseInstanceId)
