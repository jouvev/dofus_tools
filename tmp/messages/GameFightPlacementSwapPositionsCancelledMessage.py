class GameFightPlacementSwapPositionsCancelledMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
      self._cancellerIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + self.requestId + ") on element of GameFightPlacementSwapPositionsCancelledMessage.requestId.")
   
   def _cancellerIdFunc(self,input) :
      self.cancellerId = input.readDouble()
      if(self.cancellerId < -9007199254740992 or self.cancellerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.cancellerId + ") on element of GameFightPlacementSwapPositionsCancelledMessage.cancellerId.")