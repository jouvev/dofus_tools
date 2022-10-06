from src.reseau.types.EntityMovementInformations import EntityMovementInformations

class GameContextMoveMultipleElementsMessage:
   def __init__(self,input):
      self.movements = []
      _item1 = None
      _movementsLen = input.readUnsignedShort()
      for _i1 in range(0,_movementsLen):
         _item1 = EntityMovementInformations(input)
         self.movements.append(_item1)

   def resume(self):
      for e in self.movements:
         e.resume()
