from src.reseau.messages.MapComplementaryInformationsDataMessage import MapComplementaryInformationsDataMessage

class MapComplementaryInformationsWithCoordsMessage(MapComplementaryInformationsDataMessage):
   def __init__(self,input):
      super().__init__(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of MapComplementaryInformationsWithCoordsMessage.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of MapComplementaryInformationsWithCoordsMessage.worldY.")

   def resume(self):
      super().resume()
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
