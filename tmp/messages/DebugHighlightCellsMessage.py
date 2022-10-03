class DebugHighlightCellsMessage:
   def __init__(self,input):
      self.cells = []
      _val2 = 0
      self._colorFunc(input)
      _cellsLen = input.readUnsignedShort()
      for _i2 in range(0,_cellsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0 or _val2 > 559) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of cells.")
         self.cells.append(_val2)
   
   def _colorFunc(self,input) :
      self.color = input.readDouble()
      if(self.color < -9007199254740992 or self.color > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.color + ") on element of DebugHighlightCellsMessage.color.")