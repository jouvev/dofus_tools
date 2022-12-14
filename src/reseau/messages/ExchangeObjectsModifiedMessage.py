from src.reseau.messages.ExchangeObjectMessage import ExchangeObjectMessage
from src.reseau.types.ObjectItem import ObjectItem

class ExchangeObjectsModifiedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      self.object = []
      _item1 = None
      super().__init__(input)
      _objectLen = input.readUnsignedShort()
      for _i1 in range(0,_objectLen):
         _item1 = ObjectItem(input)
         self.object.append(_item1)

   def resume(self):
      super().resume()
      for e in self.object:
         e.resume()
