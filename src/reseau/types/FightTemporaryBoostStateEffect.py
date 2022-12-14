from src.reseau.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect

class FightTemporaryBoostStateEffect(FightTemporaryBoostEffect):
   def __init__(self,input):
      super().__init__(input)
      self._stateIdFunc(input)
   
   def _stateIdFunc(self,input) :
      self.stateId = input.readShort()

   def resume(self):
      super().resume()
      print("stateId :",self.stateId)
