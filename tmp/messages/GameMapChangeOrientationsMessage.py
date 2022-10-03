from tmp.types.ActorOrientation import ActorOrientation
class GameMapChangeOrientationsMessage:
   def __init__(self,input):
      self.orientations = []
      _item1 = None
      _orientationsLen = input.readUnsignedShort()
      for _i1 in range(0,_orientationsLen):
         _item1 = ActorOrientation(input)
         self.orientations.append(_item1)