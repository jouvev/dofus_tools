from tmp.types.SellerBuyerDescriptor import SellerBuyerDescriptor
from tmp.types.ObjectItemToSellInBid import ObjectItemToSellInBid
class ExchangeStartedBidSellerMessage:
   def __init__(self,input):
      self.objectsInfos = []
      _item2 = None
      self.sellerDescriptor = SellerBuyerDescriptor(input)
      _objectsInfosLen = input.readUnsignedShort()
      for _i2 in range(0,_objectsInfosLen):
         _item2 = ObjectItemToSellInBid(input)
         self.objectsInfos.append(_item2)