from src.reseau.types.ObjectItem import ObjectItem

class StorageObjectsUpdateMessage:
   def __init__(self,input):
      self.objectList = []
      _item1 = None
      _objectListLen = input.readUnsignedShort()
      for _i1 in range(0,_objectListLen):
         _item1 = ObjectItem(input)
         self.objectList.append(_item1)

   def resume(self):
      for e in self.objectList:
         e.resume()
