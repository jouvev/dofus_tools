class EntityDispositionInformations:
   def __init__(self,input):
      self._cellIdFunc(input)
      self._directionFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readShort()
      if(self.cellId < -1 or self.cellId > 559) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of EntityDispositionInformations.cellId.")
   
   def _directionFunc(self,input) :
      self.direction = input.readByte()
      if(self.direction < 0) :
         raise RuntimeError("Forbidden value (" + str(self.direction) + ") on element of EntityDispositionInformations.direction.")

   def resume(self):
      print("cellId :",self.cellId)
      print("direction :",self.direction)
