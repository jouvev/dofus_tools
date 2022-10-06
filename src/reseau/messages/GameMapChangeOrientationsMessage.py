from src.reseau.types.ActorOrientation import ActorOrientation

class GameMapChangeOrientationsMessage:
   def __init__(self,input):
      self.orientations = []
      _item1 = None
      _orientationsLen = input.readUnsignedShort()
      for _i1 in range(0,_orientationsLen):
         _item1 = ActorOrientation(input)
         self.orientations.append(_item1)

   def resume(self):
      for e in self.orientations:
         e.resume()
