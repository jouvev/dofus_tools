class GuildHouseRemoveMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + self.houseId + ") on element of GuildHouseRemoveMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + self.instanceId + ") on element of GuildHouseRemoveMessage.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()