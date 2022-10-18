import src.reseau.TypesFactory as pf
from src.reseau.types.PrismSubareaEmptyInfo import PrismSubareaEmptyInfo

class PrismGeolocalizedInformation(PrismSubareaEmptyInfo):
   def __init__(self,input):
      super().__init__(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      _id4 = input.readUnsignedShort()
      self.prism = pf.TypesFactory.get_instance_id(_id4,input)
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PrismGeolocalizedInformation.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PrismGeolocalizedInformation.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of PrismGeolocalizedInformation.mapId.")

   def resume(self):
      super().resume()
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("mapId :",self.mapId)
      self.prism.resume()
