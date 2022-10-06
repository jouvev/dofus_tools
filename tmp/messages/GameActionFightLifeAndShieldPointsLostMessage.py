from tmp.messages.GameActionFightLifePointsLostMessage import GameActionFightLifePointsLostMessage

class GameActionFightLifeAndShieldPointsLostMessage(GameActionFightLifePointsLostMessage):
   def __init__(self,input):
      super().__init__(input)
      self._shieldLossFunc(input)
   
   def _shieldLossFunc(self,input) :
      self.shieldLoss = input.readVarUhShort()
      if(self.shieldLoss < 0) :
         raise RuntimeError("Forbidden value (" + str(self.shieldLoss) + ") on element of GameActionFightLifeAndShieldPointsLostMessage.shieldLoss.")

   def resume(self):
      super().resume()
      print("shieldLoss :",self.shieldLoss)
