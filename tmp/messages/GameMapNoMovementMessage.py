class GameMapNoMovementMessage:
   def __init__(self,input):
      self._cellXFunc(input)
      self._cellYFunc(input)
   
   def _cellXFunc(self,input) :
      self.cellX = input.readShort()
   
   def _cellYFunc(self,input) :
      self.cellY = input.readShort()