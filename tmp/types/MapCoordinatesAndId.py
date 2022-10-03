from tmp.types.MapCoordinates import MapCoordinates
class MapCoordinatesAndId(MapCoordinates):
   def __init__(self,input):
      super().__init__(input)
      self._mapIdFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of MapCoordinatesAndId.mapId.")