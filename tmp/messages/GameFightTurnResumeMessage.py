from tmp.messages.GameFightTurnStartMessage import GameFightTurnStartMessage
class GameFightTurnResumeMessage(GameFightTurnStartMessage):
   def __init__(self,input):
      super().__init__(input)
      self._remainingTimeFunc(input)
   
   def _remainingTimeFunc(self,input) :
      self.remainingTime = input.readVarUhInt()
      if(self.remainingTime < 0) :
         raise RuntimeError("Forbidden value (" + self.remainingTime + ") on element of GameFightTurnResumeMessage.remainingTime.")