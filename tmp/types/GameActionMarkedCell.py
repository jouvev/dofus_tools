class GameActionMarkedCell:
   def __init__(self,input):
      self._cellIdFunc(input)
      self._zoneSizeFunc(input)
      self._cellColorFunc(input)
      self._cellsTypeFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of GameActionMarkedCell.cellId.")
   
   def _zoneSizeFunc(self,input) :
      self.zoneSize = input.readByte()
   
   def _cellColorFunc(self,input) :
      self.cellColor = input.readInt()
   
   def _cellsTypeFunc(self,input) :
      self.cellsType = input.readByte()

   def resume(self):
      print("cellId :",self.cellId)
      print("zoneSize :",self.zoneSize)
      print("cellColor :",self.cellColor)
      print("cellsType :",self.cellsType)
