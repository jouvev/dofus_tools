class GameFightPlacementSwapPositionsOfferMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
      self._requesterIdFunc(input)
      self._requesterCellIdFunc(input)
      self._requestedIdFunc(input)
      self._requestedCellIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + self.requestId + ") on element of GameFightPlacementSwapPositionsOfferMessage.requestId.")
   
   def _requesterIdFunc(self,input) :
      self.requesterId = input.readDouble()
      if(self.requesterId < -9007199254740992 or self.requesterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.requesterId + ") on element of GameFightPlacementSwapPositionsOfferMessage.requesterId.")
   
   def _requesterCellIdFunc(self,input) :
      self.requesterCellId = input.readVarUhShort()
      if(self.requesterCellId < 0 or self.requesterCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.requesterCellId + ") on element of GameFightPlacementSwapPositionsOfferMessage.requesterCellId.")
   
   def _requestedIdFunc(self,input) :
      self.requestedId = input.readDouble()
      if(self.requestedId < -9007199254740992 or self.requestedId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.requestedId + ") on element of GameFightPlacementSwapPositionsOfferMessage.requestedId.")
   
   def _requestedCellIdFunc(self,input) :
      self.requestedCellId = input.readVarUhShort()
      if(self.requestedCellId < 0 or self.requestedCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.requestedCellId + ") on element of GameFightPlacementSwapPositionsOfferMessage.requestedCellId.")