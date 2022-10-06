from tmp.types.HouseInformationsForSell import HouseInformationsForSell

class HouseToSellListMessage:
   def __init__(self,input):
      self.houseList = []
      _item3 = None
      self._pageIndexFunc(input)
      self._totalPageFunc(input)
      _houseListLen = input.readUnsignedShort()
      for _i3 in range(0,_houseListLen):
         _item3 = HouseInformationsForSell(input)
         self.houseList.append(_item3)
   
   def _pageIndexFunc(self,input) :
      self.pageIndex = input.readVarUhShort()
      if(self.pageIndex < 0) :
         raise RuntimeError("Forbidden value (" + str(self.pageIndex) + ") on element of HouseToSellListMessage.pageIndex.")
   
   def _totalPageFunc(self,input) :
      self.totalPage = input.readVarUhShort()
      if(self.totalPage < 0) :
         raise RuntimeError("Forbidden value (" + str(self.totalPage) + ") on element of HouseToSellListMessage.totalPage.")

   def resume(self):
      print("pageIndex :",self.pageIndex)
      print("totalPage :",self.totalPage)
      for e in self.houseList:
         e.resume()
