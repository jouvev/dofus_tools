class ObjectGroundRemovedMultipleMessage:
   def __init__(self,input):
      self.cells = []
      _val1 = 0
      _cellsLen = input.readUnsignedShort()
      for _i1 in range(0,_cellsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0 or _val1 > 559) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of cells.")
         self.cells.append(_val1)

   def resume(self):
      print("cells :",self.cells)
