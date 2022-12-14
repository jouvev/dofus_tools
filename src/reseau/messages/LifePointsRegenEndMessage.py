from src.reseau.messages.UpdateLifePointsMessage import UpdateLifePointsMessage

class LifePointsRegenEndMessage(UpdateLifePointsMessage):
   def __init__(self,input):
      super().__init__(input)
      self._lifePointsGainedFunc(input)
   
   def _lifePointsGainedFunc(self,input) :
      self.lifePointsGained = input.readVarUhInt()
      if(self.lifePointsGained < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lifePointsGained) + ") on element of LifePointsRegenEndMessage.lifePointsGained.")

   def resume(self):
      super().resume()
      print("lifePointsGained :",self.lifePointsGained)
