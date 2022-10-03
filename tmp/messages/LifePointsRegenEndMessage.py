from tmp.messages.UpdateLifePointsMessage import UpdateLifePointsMessage
class LifePointsRegenEndMessage(UpdateLifePointsMessage):
   def __init__(self,input):
      super().__init__(input)
      self._lifePointsGainedFunc(input)
   
   def _lifePointsGainedFunc(self,input) :
      self.lifePointsGained = input.readVarUhInt()
      if(self.lifePointsGained < 0) :
         raise RuntimeError("Forbidden value (" + self.lifePointsGained + ") on element of LifePointsRegenEndMessage.lifePointsGained.")