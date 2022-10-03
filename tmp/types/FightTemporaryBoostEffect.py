from tmp.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect
class FightTemporaryBoostEffect(AbstractFightDispellableEffect):
   def __init__(self,input):
      super().__init__(input)
      self._deltaFunc(input)
   
   def _deltaFunc(self,input) :
      self.delta = input.readInt()