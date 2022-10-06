from src.reseau.types.TreasureHuntStep import TreasureHuntStep

class TreasureHuntStepFollowDirection(TreasureHuntStep):
   def __init__(self,input):
      super().__init__(input)
      self._directionFunc(input)
      self._mapCountFunc(input)
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of TreasureHuntStepFollowDirection.direction.")
   
   def _mapCountFunc(self,input) :
      self.mapCount = input.readVarUhShort()
      if(self.mapCount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.mapCount) + ") on element of TreasureHuntStepFollowDirection.mapCount.")

   def resume(self):
      super().resume()
      print("direction :",self.direction)
      print("mapCount :",self.mapCount)
