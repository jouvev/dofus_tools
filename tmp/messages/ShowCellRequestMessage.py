class ShowCellRequestMessage:
   def __init__(self,input):
      self._cellIdFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of ShowCellRequestMessage.cellId.")

   def resume(self):
      print("cellId :",self.cellId)
