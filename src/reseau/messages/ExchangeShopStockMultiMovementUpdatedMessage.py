from src.reseau.types.ObjectItemToSell import ObjectItemToSell

class ExchangeShopStockMultiMovementUpdatedMessage:
   def __init__(self,input):
      self.objectInfoList = []
      _item1 = None
      _objectInfoListLen = input.readUnsignedShort()
      for _i1 in range(0,_objectInfoListLen):
         _item1 = ObjectItemToSell(input)
         self.objectInfoList.append(_item1)

   def resume(self):
      for e in self.objectInfoList:
         e.resume()
