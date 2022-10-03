class PaddockMoveItemRequestMessage:
   def __init__(self,input):
      self._oldCellIdFunc(input)
      self._newCellIdFunc(input)
   
   def _oldCellIdFunc(self,input) :
      self.oldCellId = input.readVarUhShort()
      if(self.oldCellId < 0 or self.oldCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.oldCellId + ") on element of PaddockMoveItemRequestMessage.oldCellId.")
   
   def _newCellIdFunc(self,input) :
      self.newCellId = input.readVarUhShort()
      if(self.newCellId < 0 or self.newCellId > 559) :
         raise RuntimeError("Forbidden value (" + self.newCellId + ") on element of PaddockMoveItemRequestMessage.newCellId.")