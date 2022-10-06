class GameFightPlacementSwapPositionsCancelMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.requestId) + ") on element of GameFightPlacementSwapPositionsCancelMessage.requestId.")

   def resume(self):
      print("requestId :",self.requestId)
