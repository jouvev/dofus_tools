class ChallengeTargetsListMessage:
   def __init__(self,input):
      self.targetIds = []
      self.targetCells = []
      _val1 = None
      _val2 = 0
      _targetIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_targetIdsLen):
         _val1 = input.readDouble()
         if(_val1 < -9007199254740992 or _val1 > 9007199254740992) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of targetIds.")
         self.targetIds.append(_val1)
      _targetCellsLen = input.readUnsignedShort()
      for _i2 in range(0,_targetCellsLen):
         _val2 = input.readShort()
         if(_val2 < -1 or _val2 > 559) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of targetCells.")
         self.targetCells.append(_val2)

   def resume(self):
      print("targetIds :",self.targetIds)
      print("targetCells :",self.targetCells)
