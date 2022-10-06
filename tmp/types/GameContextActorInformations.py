from tmp.types.EntityLook import EntityLook
from tmp.types.GameContextActorPositionInformations import GameContextActorPositionInformations

class GameContextActorInformations(GameContextActorPositionInformations):
   def __init__(self,input):
      super().__init__(input)
      self.look = EntityLook(input)

   def resume(self):
      super().resume()
      self.look.resum()
