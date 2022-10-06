from tmp.types.ObjectItemGenericQuantity import ObjectItemGenericQuantity

class ExchangeBidHouseUnsoldItemsMessage:
   def __init__(self,input):
      self.items = []
      _item1 = None
      _itemsLen = input.readUnsignedShort()
      for _i1 in range(0,_itemsLen):
         _item1 = ObjectItemGenericQuantity(input)
         self.items.append(_item1)

   def resume(self):
      for e in self.items:
         e.resume()
