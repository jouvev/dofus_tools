from src.reseau.types.ObjectItemToSellInHumanVendorShop import ObjectItemToSellInHumanVendorShop

class ExchangeStartOkHumanVendorMessage:
   def __init__(self,input):
      self.objectsInfos = []
      _item2 = None
      self._sellerIdFunc(input)
      _objectsInfosLen = input.readUnsignedShort()
      for _i2 in range(0,_objectsInfosLen):
         _item2 = ObjectItemToSellInHumanVendorShop(input)
         self.objectsInfos.append(_item2)
   
   def _sellerIdFunc(self,input) :
      self.sellerId = input.readDouble()
      if(self.sellerId < -9007199254740992 or self.sellerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.sellerId) + ") on element of ExchangeStartOkHumanVendorMessage.sellerId.")

   def resume(self):
      print("sellerId :",self.sellerId)
      for e in self.objectsInfos:
         e.resume()
