from src.reseau.types.StatedElement import StatedElement

class StatedElementUpdatedMessage:
   def __init__(self,input):
      self.statedElement = StatedElement(input)

   def resume(self):
      self.statedElement.resum()
