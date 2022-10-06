from tmp.types.PaddockInformationsForSell import PaddockInformationsForSell

class PaddockToSellListMessage:
   def __init__(self,input):
      self.paddockList = []
      _item3 = None
      self._pageIndexFunc(input)
      self._totalPageFunc(input)
      _paddockListLen = input.readUnsignedShort()
      for _i3 in range(0,_paddockListLen):
         _item3 = PaddockInformationsForSell(input)
         self.paddockList.append(_item3)
   
   def _pageIndexFunc(self,input) :
      self.pageIndex = input.readVarUhShort()
      if(self.pageIndex < 0) :
         raise RuntimeError("Forbidden value (" + str(self.pageIndex) + ") on element of PaddockToSellListMessage.pageIndex.")
   
   def _totalPageFunc(self,input) :
      self.totalPage = input.readVarUhShort()
      if(self.totalPage < 0) :
         raise RuntimeError("Forbidden value (" + str(self.totalPage) + ") on element of PaddockToSellListMessage.totalPage.")

   def resume(self):
      print("pageIndex :",self.pageIndex)
      print("totalPage :",self.totalPage)
      for e in self.paddockList:
         e.resume()
