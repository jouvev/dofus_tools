from tmp.types.AccountTagInformation import AccountTagInformation
from tmp.types.HouseInformations import HouseInformations
class HouseInformationsForGuild(HouseInformations):
   def __init__(self,input):
      self.skillListIds = []
      _val8 = 0
      super().__init__(input)
      self._instanceIdFunc(input)
      self._secondHandFunc(input)
      self.ownerTag = AccountTagInformation(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      _skillListIdsLen = input.readUnsignedShort()
      for _i8 in range(0,_skillListIdsLen):
         _val8 = input.readInt()
         self.skillListIds.append(_val8)
      self._guildshareParamsFunc(input)
   
   def _instanceIdFunc(self,input) :
      self.instanceId = input.readInt()
      if(self.instanceId < 0) :
         raise RuntimeError("Forbidden value (" + self.instanceId + ") on element of HouseInformationsForGuild.instanceId.")
   
   def _secondHandFunc(self,input) :
      self.secondHand = input.readBoolean()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of HouseInformationsForGuild.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of HouseInformationsForGuild.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of HouseInformationsForGuild.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of HouseInformationsForGuild.subAreaId.")
   
   def _guildshareParamsFunc(self,input) :
      self.guildshareParams = input.readVarUhInt()
      if(self.guildshareParams < 0) :
         raise RuntimeError("Forbidden value (" + self.guildshareParams + ") on element of HouseInformationsForGuild.guildshareParams.")