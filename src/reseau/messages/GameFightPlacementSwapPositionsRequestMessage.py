from src.reseau.messages.GameFightPlacementPositionRequestMessage import GameFightPlacementPositionRequestMessage

class GameFightPlacementSwapPositionsRequestMessage(GameFightPlacementPositionRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._requestedIdFunc(input)
   
   def _requestedIdFunc(self,input) :
      self.requestedId = input.readDouble()
      if(self.requestedId < -9007199254740992 or self.requestedId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.requestedId) + ") on element of GameFightPlacementSwapPositionsRequestMessage.requestedId.")

   def resume(self):
      super().resume()
      print("requestedId :",self.requestedId)
