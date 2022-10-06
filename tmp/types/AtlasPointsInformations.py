from tmp.types.MapCoordinatesExtended import MapCoordinatesExtended

class AtlasPointsInformations:
   def __init__(self,input):
      self.coords = []
      _item2 = None
      self._typeFunc(input)
      _coordsLen = input.readUnsignedShort()
      for _i2 in range(0,_coordsLen):
         _item2 = MapCoordinatesExtended(input)
         self.coords.append(_item2)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + str(self.type) + ") on element of AtlasPointsInformations.type.")

   def resume(self):
      print("type :",self.type)
      for e in self.coords:
         e.resume()
