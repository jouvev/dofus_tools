class GameMapChangeOrientationRequestMessage:
   def __init__(self,input):
      self._directionFunc(input)
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + self.direction + ") on element of GameMapChangeOrientationRequestMessage.direction.")