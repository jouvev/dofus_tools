from src.reseau.types.ObjectItem import ObjectItem

class StorageObjectUpdateMessage:
   def __init__(self,input):
      self.object = ObjectItem(input)

   def resume(self):
      self.object.resum()
