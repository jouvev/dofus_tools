from src.reseau.types.EntityMovementInformations import EntityMovementInformations

class GameContextMoveElementMessage:
   def __init__(self,input):
      self.movement = EntityMovementInformations(input)

   def resume(self):
      self.movement.resume()
