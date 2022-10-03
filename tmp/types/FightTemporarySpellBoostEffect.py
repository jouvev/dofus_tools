from tmp.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect
class FightTemporarySpellBoostEffect(FightTemporaryBoostEffect):
   def __init__(self,input):
      super().__init__(input)
      self._boostedSpellIdFunc(input)
   
   def _boostedSpellIdFunc(self,input) :
      self.boostedSpellId = input.readVarUhShort()
      if(self.boostedSpellId < 0) :
         raise RuntimeError("Forbidden value (" + self.boostedSpellId + ") on element of FightTemporarySpellBoostEffect.boostedSpellId.")