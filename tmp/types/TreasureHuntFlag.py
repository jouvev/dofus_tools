class TreasureHuntFlag:
   def __init__(self,input):
      self._mapIdFunc(input)
      self._stateFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of TreasureHuntFlag.mapId.")
   
   def _stateFunc(self,input) :
      self.state = input.readByte()
      if(self.state < 0) :
         raise RuntimeError("Forbidden value (" + self.state + ") on element of TreasureHuntFlag.state.")