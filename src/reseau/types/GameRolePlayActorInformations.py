from src.reseau.types.GameContextActorInformations import GameContextActorInformations

class GameRolePlayActorInformations(GameContextActorInformations):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
