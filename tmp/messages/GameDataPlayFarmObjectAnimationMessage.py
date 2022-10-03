class GameDataPlayFarmObjectAnimationMessage:
   def __init__(self,input):
      self.cellId = []
      _val1 = 0
      _cellIdLen = input.readUnsignedShort()
      for _i1 in range(0,_cellIdLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0 or _val1 > 559) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of cellId.")
         self.cellId.append(_val1)