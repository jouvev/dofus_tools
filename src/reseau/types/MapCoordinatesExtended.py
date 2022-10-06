from src.reseau.types.MapCoordinatesAndId import MapCoordinatesAndId

class MapCoordinatesExtended(MapCoordinatesAndId):
   def __init__(self,input):
      super().__init__(input)
      self._subAreaIdFunc(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of MapCoordinatesExtended.subAreaId.")

   def resume(self):
      super().resume()
      print("subAreaId :",self.subAreaId)
