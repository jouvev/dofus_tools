class ShowCellMessage:
   def __init__(self,input):
      self._sourceIdFunc(input)
      self._cellIdFunc(input)
   
   def _sourceIdFunc(self,input) :
      self.sourceId = input.readDouble()
      if(self.sourceId < -9007199254740992 or self.sourceId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sourceId) + ") on element of ShowCellMessage.sourceId.")
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of ShowCellMessage.cellId.")

   def resume(self):
      print("sourceId :",self.sourceId)
      print("cellId :",self.cellId)
