from tmp.types.TreasureHuntStep import TreasureHuntStep
class TreasureHuntStepFollowDirectionToHint(TreasureHuntStep):
   def __init__(self,input):
      super().__init__(input)
      self._directionFunc(input)
      self._npcIdFunc(input)
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + self.direction + ") on element of TreasureHuntStepFollowDirectionToHint.direction.")
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readVarUhShort()
      if(self.npcId < 0) :
         raise RuntimeError("Forbidden value (" + self.npcId + ") on element of TreasureHuntStepFollowDirectionToHint.npcId.")