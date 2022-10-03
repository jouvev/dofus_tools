class PaddockToSellFilterMessage:
   def __init__(self,input):
      self._areaIdFunc(input)
      self._atLeastNbMountFunc(input)
      self._atLeastNbMachineFunc(input)
      self._maxPriceFunc(input)
      self._orderByFunc(input)
   
   def _areaIdFunc(self,input) :
      self.areaId = input.readInt()
   
   def _atLeastNbMountFunc(self,input) :
      self.atLeastNbMount = input.readByte()
   
   def _atLeastNbMachineFunc(self,input) :
      self.atLeastNbMachine = input.readByte()
   
   def _maxPriceFunc(self,input) :
      self.maxPrice = input.readVarUhLong()
      if(self.maxPrice < 0 or self.maxPrice > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.maxPrice + ") on element of PaddockToSellFilterMessage.maxPrice.")
   
   def _orderByFunc(self,input) :
      self.orderBy = input.readByte()
      if(self.orderBy < 0) :
         raise RuntimeError("Forbidden value (" + self.orderBy + ") on element of PaddockToSellFilterMessage.orderBy.")