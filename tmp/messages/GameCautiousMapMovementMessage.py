from tmp.messages.GameMapMovementMessage import GameMapMovementMessage
class GameCautiousMapMovementMessage(GameMapMovementMessage):
   def __init__(self,input):
      super().__init__(input)