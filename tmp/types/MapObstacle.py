class MapObstacle:
   def __init__(self,input):
      self._obstacleCellIdFunc(input)
      self._stateFunc(input)
   
   def _obstacleCellIdFunc(self,input) :
      self.obstacleCellId = input.readVarUhShort()
      if(self.obstacleCellId < 0 or self.obstacleCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.obstacleCellId + ") on element of MapObstacle.obstacleCellId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of MapObstacle.state.")