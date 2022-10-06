class PaddockInformations:
   def __init__(self,input):
      self._maxOutdoorMountFunc(input)
      self._maxItemsFunc(input)
   
   def _maxOutdoorMountFunc(self,input) :
      self.maxOutdoorMount = input.readVarUhShort()
      if(self.maxOutdoorMount < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxOutdoorMount) + ") on element of PaddockInformations.maxOutdoorMount.")
   
   def _maxItemsFunc(self,input) :
      self.maxItems = input.readVarUhShort()
      if(self.maxItems < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxItems) + ") on element of PaddockInformations.maxItems.")

   def resume(self):
      print("maxOutdoorMount :",self.maxOutdoorMount)
      print("maxItems :",self.maxItems)
