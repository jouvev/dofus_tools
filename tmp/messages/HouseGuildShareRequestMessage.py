class HouseGuildShareRequestMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._enableFunc(input)
      self._rightsFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + self.houseId + ") on element of HouseGuildShareRequestMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + self.instanceId + ") on element of HouseGuildShareRequestMessage.instanceId.")
   
   def _enableFunc(self,input) :
      self.enable = input.readBoolean()
   
   def _rightsFunc(self,input) :
      self.rights = input.readVarUhInt()
      if(self.rights < 0) :
         raise RuntimeError("Forbidden value (" + self.rights + ") on element of HouseGuildShareRequestMessage.rights.")