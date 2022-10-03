from tmp.types.StatedElement import StatedElement
class StatedElementUpdatedMessage:
   def __init__(self,input):
      self.statedElement = StatedElement(input)