from src.reseau.types.StatedElement import StatedElement

class StatedMapUpdateMessage:
   def __init__(self,input):
      self.statedElements = []
      _item1 = None
      _statedElementsLen = input.readUnsignedShort()
      for _i1 in range(0,_statedElementsLen):
         _item1 = StatedElement(input)
         self.statedElements.append(_item1)

   def resume(self):
      for e in self.statedElements:
         e.resume()
