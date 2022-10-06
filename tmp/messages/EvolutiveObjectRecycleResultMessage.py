from tmp.types.RecycledItem import RecycledItem

class EvolutiveObjectRecycleResultMessage:
   def __init__(self,input):
      self.recycledItems = []
      _item1 = None
      _recycledItemsLen = input.readUnsignedShort()
      for _i1 in range(0,_recycledItemsLen):
         _item1 = RecycledItem(input)
         self.recycledItems.append(_item1)

   def resume(self):
      for e in self.recycledItems:
         e.resume()
