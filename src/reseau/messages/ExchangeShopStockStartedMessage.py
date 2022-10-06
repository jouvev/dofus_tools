from src.reseau.types.ObjectItemToSell import ObjectItemToSell

class ExchangeShopStockStartedMessage:
   def __init__(self,input):
      self.objectsInfos = []
      _item1 = None
      _objectsInfosLen = input.readUnsignedShort()
      for _i1 in range(0,_objectsInfosLen):
         _item1 = ObjectItemToSell(input)
         self.objectsInfos.append(_item1)

   def resume(self):
      for e in self.objectsInfos:
         e.resume()
