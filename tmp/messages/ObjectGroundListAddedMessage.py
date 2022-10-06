class ObjectGroundListAddedMessage:
   def __init__(self,input):
      self.cells = []
      self.referenceIds = []
      _val1 = 0
      _val2 = 0
      _cellsLen = input.readUnsignedShort()
      for _i1 in range(0,_cellsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0 or _val1 > 559) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of cells.")
         self.cells.append(_val1)
      _referenceIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_referenceIdsLen):
         _val2 = input.readVarUhInt()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of referenceIds.")
         self.referenceIds.append(_val2)

   def resume(self):
      print("cells :",self.cells)
      print("referenceIds :",self.referenceIds)
