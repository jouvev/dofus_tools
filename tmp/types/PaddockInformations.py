class PaddockInformations:
   def __init__(self,input):
      self._maxOutdoorMountFunc(input)
      self._maxItemsFunc(input)
   
   def _maxOutdoorMountFunc(self,input) :
      self.maxOutdoorMount = input.readVarUhShort()
      if(self.maxOutdoorMount < 0) :
         raise RuntimeError("Forbidden value (" + self.maxOutdoorMount + ") on element of PaddockInformations.maxOutdoorMount.")
   
   def _maxItemsFunc(self,input) :
      self.maxItems = input.readVarUhShort()
      if(self.maxItems < 0) :
         raise RuntimeError("Forbidden value (" + self.maxItems + ") on element of PaddockInformations.maxItems.")