from tmp.types.ObjectItem import ObjectItem
class StorageObjectUpdateMessage:
   def __init__(self,input):
      self.object = ObjectItem(input)