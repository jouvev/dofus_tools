from tmp.types.MapObstacle import MapObstacle
class MapObstacleUpdateMessage:
   def __init__(self,input):
      self.obstacles = []
      _item1 = None
      _obstaclesLen = input.readUnsignedShort()
      for _i1 in range(0,_obstaclesLen):
         _item1 = MapObstacle(input)
         self.obstacles.append(_item1)