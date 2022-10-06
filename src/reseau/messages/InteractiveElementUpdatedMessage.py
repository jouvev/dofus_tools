from src.reseau.types.InteractiveElement import InteractiveElement

class InteractiveElementUpdatedMessage:
   def __init__(self,input):
      self.interactiveElement = InteractiveElement(input)

   def resume(self):
      self.interactiveElement.resum()
