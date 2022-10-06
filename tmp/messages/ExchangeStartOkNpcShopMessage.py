from tmp.types.ObjectItemToSellInNpcShop import ObjectItemToSellInNpcShop

class ExchangeStartOkNpcShopMessage:
   def __init__(self,input):
      self.objectsInfos = []
      _item3 = None
      self._npcSellerIdFunc(input)
      self._tokenIdFunc(input)
      _objectsInfosLen = input.readUnsignedShort()
      for _i3 in range(0,_objectsInfosLen):
         _item3 = ObjectItemToSellInNpcShop(input)
         self.objectsInfos.append(_item3)
   
   def _npcSellerIdFunc(self,input) :
      self.npcSellerId = input.readDouble()
      if(self.npcSellerId < -9007199254740992 or self.npcSellerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.npcSellerId) + ") on element of ExchangeStartOkNpcShopMessage.npcSellerId.")
   
   def _tokenIdFunc(self,input) :
      self.tokenId = input.readVarUhInt()
      if(self.tokenId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.tokenId) + ") on element of ExchangeStartOkNpcShopMessage.tokenId.")

   def resume(self):
      print("npcSellerId :",self.npcSellerId)
      print("tokenId :",self.tokenId)
      for e in self.objectsInfos:
         e.resume()
