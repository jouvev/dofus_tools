from src.reseau.types.GameFightFighterInformations import GameFightFighterInformations

class GameFightAIInformations(GameFightFighterInformations):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
