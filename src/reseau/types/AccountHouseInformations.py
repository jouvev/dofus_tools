import src.reseau.TypesFactory as pf
from src.reseau.types.HouseInformations import HouseInformations

class AccountHouseInformations(HouseInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.houseInfos = pf.TypesFactory.get_instance_id(_id1,input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of AccountHouseInformations.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of AccountHouseInformations.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of AccountHouseInformations.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of AccountHouseInformations.subAreaId.")

   def resume(self):
      super().resume()
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("mapId :",self.mapId)
      print("subAreaId :",self.subAreaId)
