from tmp.types.TreasureHuntStep import TreasureHuntStep
class TreasureHuntStepFollowDirectionToPOI(TreasureHuntStep):
   def __init__(self,input):
      super().__init__(input)
      self._directionFunc(input)
      self._poiLabelIdFunc(input)
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + self.direction + ") on element of TreasureHuntStepFollowDirectionToPOI.direction.")
   
   def _poiLabelIdFunc(self,input) :
      self.poiLabelId = input.readVarUhShort()
      if(self.poiLabelId < 0) :
         raise RuntimeError("Forbidden value (" + self.poiLabelId + ") on element of TreasureHuntStepFollowDirectionToPOI.poiLabelId.")