class FightStartingPositions:
   def __init__(self,input):
      self.positionsForChallengers = []
      self.positionsForDefenders = []
      _val1 = 0
      _val2 = 0
      _positionsForChallengersLen = input.readUnsignedShort()
      for _i1 in range(0,_positionsForChallengersLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0 or _val1 > 559) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of positionsForChallengers.")
         self.positionsForChallengers.append(_val1)
      _positionsForDefendersLen = input.readUnsignedShort()
      for _i2 in range(0,_positionsForDefendersLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0 or _val2 > 559) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of positionsForDefenders.")
         self.positionsForDefenders.append(_val2)

   def resume(self):
      print("positionsForChallengers :",self.positionsForChallengers)
      print("positionsForDefenders :",self.positionsForDefenders)
