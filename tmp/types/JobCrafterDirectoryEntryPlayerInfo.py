import tmp.TypesFactory as pf
class JobCrafterDirectoryEntryPlayerInfo:
   def __init__(self,input):
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._alignmentSideFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self._isInWorkshopFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      self._canCraftLegendaryFunc(input)
      _id12 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id12,input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of JobCrafterDirectoryEntryPlayerInfo.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 0 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + self.breed + ") on element of JobCrafterDirectoryEntryPlayerInfo.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _isInWorkshopFunc(self,input) :
      self.isInWorkshop = input.readBoolean()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of JobCrafterDirectoryEntryPlayerInfo.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of JobCrafterDirectoryEntryPlayerInfo.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of JobCrafterDirectoryEntryPlayerInfo.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of JobCrafterDirectoryEntryPlayerInfo.subAreaId.")
   
   def _canCraftLegendaryFunc(self,input) :
      self.canCraftLegendary = input.readBoolean()