from src.reseau.messages.GameFightShowFighterMessage import GameFightShowFighterMessage

class GameFightShowFighterRandomStaticPoseMessage(GameFightShowFighterMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
