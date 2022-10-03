class HouseToSellListRequestMessage:
   def __init__(self,input):
      self._pageIndexFunc(input)
   
   def _pageIndexFunc(self,input) :
      self.pageIndex = input.readVarUhShort()
      if(self.pageIndex < 0) :
         raise RuntimeError("Forbidden value (" + self.pageIndex + ") on element of HouseToSellListRequestMessage.pageIndex.")