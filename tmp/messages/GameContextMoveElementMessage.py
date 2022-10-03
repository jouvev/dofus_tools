from tmp.types.EntityMovementInformations import EntityMovementInformations
class GameContextMoveElementMessage:
   def __init__(self,input):
      self.movement = EntityMovementInformations(input)