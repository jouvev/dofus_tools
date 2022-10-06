class GameMapMovementMessage:
   def __init__(self,input):
      self.keyMovements = []
      _val1 = 0
      _keyMovementsLen = input.readUnsignedShort()
      for _i1 in range(0,_keyMovementsLen):
         _val1 = input.readShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of keyMovements.")
         self.keyMovements.append(_val1)
      self._forcedDirectionFunc(input)
      self._actorIdFunc(input)
   
   def _forcedDirectionFunc(self,input) :
      self.forcedDirection = input.readShort()
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.actorId) + ") on element of GameMapMovementMessage.actorId.")

   def resume(self):
      print("forcedDirection :",self.forcedDirection)
      print("actorId :",self.actorId)
      print("keyMovements :",self.keyMovements)
