class HouseGuildRightsViewMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.houseId) + ") on element of HouseGuildRightsViewMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.instanceId) + ") on element of HouseGuildRightsViewMessage.instanceId.")

   def resume(self):
      print("houseId :",self.houseId)
      print("instanceId :",self.instanceId)
