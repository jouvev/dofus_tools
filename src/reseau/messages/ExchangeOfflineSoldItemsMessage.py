from src.reseau.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects
from src.reseau.types.ObjectItemQuantityPriceDateEffects import ObjectItemQuantityPriceDateEffects

class ExchangeOfflineSoldItemsMessage:
   def __init__(self,input):
      self.bidHouseItems = []
      self.merchantItems = []
      _item1 = None
      _item2 = None
      _bidHouseItemsLen = input.readUnsignedShort()
      for _i1 in range(0,_bidHouseItemsLen):
         _item1 = ObjectItemQuantityPriceDateEffects(input)
         self.bidHouseItems.append(_item1)
      _merchantItemsLen = input.readUnsignedShort()
      for _i2 in range(0,_merchantItemsLen):
         _item2 = ObjectItemQuantityPriceDateEffects(input)
         self.merchantItems.append(_item2)

   def resume(self):
      for e in self.bidHouseItems:
         e.resume()
      for e in self.merchantItems:
         e.resume()
