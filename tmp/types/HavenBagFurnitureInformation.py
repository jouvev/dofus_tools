class HavenBagFurnitureInformation:
   def __init__(self,input):
      self._cellIdFunc(input)
      self._funitureIdFunc(input)
      self._orientationFunc(input)
   
   def _cellIdFunc(self,input) :
      self.cellId = input.readVarUhShort()
      if(self.cellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.cellId) + ") on element of HavenBagFurnitureInformation.cellId.")
   
   def _funitureIdFunc(self,input) :
      self.funitureId = input.readInt()
   
   def _orientationFunc(self,input) :
      self.orientation = input.readByte()
      if(self.orientation < 0) :
         raise RuntimeError("Forbidden value (" + str(self.orientation) + ") on element of HavenBagFurnitureInformation.orientation.")

   def resume(self):
      print("cellId :",self.cellId)
      print("funitureId :",self.funitureId)
      print("orientation :",self.orientation)
