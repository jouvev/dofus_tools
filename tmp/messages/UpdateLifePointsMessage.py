class UpdateLifePointsMessage:
   def __init__(self,input):
      self._lifePointsFunc(input)
      self._maxLifePointsFunc(input)
   
   def _lifePointsFunc(self,input) :
      self.lifePoints = input.readVarUhInt()
      if(self.lifePoints < 0) :
         raise RuntimeError("Forbidden value (" + self.lifePoints + ") on element of UpdateLifePointsMessage.lifePoints.")
   
   def _maxLifePointsFunc(self,input) :
      self.maxLifePoints = input.readVarUhInt()
      if(self.maxLifePoints < 0) :
         raise RuntimeError("Forbidden value (" + self.maxLifePoints + ") on element of UpdateLifePointsMessage.maxLifePoints.")