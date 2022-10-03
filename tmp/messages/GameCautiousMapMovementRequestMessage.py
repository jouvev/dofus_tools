from tmp.messages.GameMapMovementRequestMessage import GameMapMovementRequestMessage
class GameCautiousMapMovementRequestMessage(GameMapMovementRequestMessage):
   def __init__(self,input):
      super().__init__(input)