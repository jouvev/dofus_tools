class GameFightPlacementSwapPositionsAcceptMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + self.requestId + ") on element of GameFightPlacementSwapPositionsAcceptMessage.requestId.")