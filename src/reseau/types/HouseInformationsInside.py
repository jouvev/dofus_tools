import src.reseau.TypesFactory as pf
from src.reseau.types.HouseInformations import HouseInformations

class HouseInformationsInside(HouseInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.houseInfos = pf.TypesFactory.get_instance_id(_id1,input)
      self._worldXFunc(input)
      self._worldYFunc(input)
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of HouseInformationsInside.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of HouseInformationsInside.worldY.")

   def resume(self):
      super().resume()
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
