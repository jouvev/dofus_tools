from src.reseau.types.ObjectItem import ObjectItem

class MimicryObjectPreviewMessage:
   def __init__(self,input):
      self.result = ObjectItem(input)

   def resume(self):
      self.result.resum()
