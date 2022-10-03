class GameMapMovementRequestMessage:
   def __init__(self,input):
      self.keyMovements = []
      _val1 = 0
      _keyMovementsLen = input.readUnsignedShort()
      for _i1 in range(0,_keyMovementsLen):
         _val1 = input.readShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of keyMovements.")
         self.keyMovements.append(_val1)
      self._mapIdFunc(input)
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of GameMapMovementRequestMessage.mapId.")