from tmp.types.ObjectItem import ObjectItem

class ObjectModifiedMessage:
   def __init__(self,input):
      self.object = ObjectItem(input)

   def resume(self):
      self.object.resum()
