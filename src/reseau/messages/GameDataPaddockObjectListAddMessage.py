from src.reseau.types.PaddockItem import PaddockItem

class GameDataPaddockObjectListAddMessage:
   def __init__(self,input):
      self.paddockItemDescription = []
      _item1 = None
      _paddockItemDescriptionLen = input.readUnsignedShort()
      for _i1 in range(0,_paddockItemDescriptionLen):
         _item1 = PaddockItem(input)
         self.paddockItemDescription.append(_item1)

   def resume(self):
      for e in self.paddockItemDescription:
         e.resume()
