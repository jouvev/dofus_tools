from src.reseau.types.ObjectItem import ObjectItem

class ObjectsAddedMessage:
   def __init__(self,input):
      self.object = []
      _item1 = None
      _objectLen = input.readUnsignedShort()
      for _i1 in range(0,_objectLen):
         _item1 = ObjectItem(input)
         self.object.append(_item1)

   def resume(self):
      for e in self.object:
         e.resume()
