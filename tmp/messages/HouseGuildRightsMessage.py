from tmp.types.GuildInformations import GuildInformations
class HouseGuildRightsMessage:
   def __init__(self,input):
      self._houseIdFunc(input)
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
      self.guildInfo = GuildInformations(input)
      self._rightsFunc(input)
   
   def _houseIdFunc(self,input) :
      self.houseId = input.readVarUhInt()
      if(self.houseId < 0) :
         raise RuntimeError("Forbidden value (" + self.houseId + ") on element of HouseGuildRightsMessage.houseId.")
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + self.instanceId + ") on element of HouseGuildRightsMessage.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()
   
   def _rightsFunc(self,input) :
      self.rights = input.readVarUhInt()
      if(self.rights < 0) :
         raise RuntimeError("Forbidden value (" + self.rights + ") on element of HouseGuildRightsMessage.rights.")