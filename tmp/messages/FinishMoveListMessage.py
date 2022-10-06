from tmp.types.FinishMoveInformations import FinishMoveInformations

class FinishMoveListMessage:
   def __init__(self,input):
      self.finishMoves = []
      _item1 = None
      _finishMovesLen = input.readUnsignedShort()
      for _i1 in range(0,_finishMovesLen):
         _item1 = FinishMoveInformations(input)
         self.finishMoves.append(_item1)

   def resume(self):
      for e in self.finishMoves:
         e.resume()
