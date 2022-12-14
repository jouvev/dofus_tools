from src.reseau.types.AbstractFightDispellableEffect import AbstractFightDispellableEffect

class FightTemporarySpellImmunityEffect(AbstractFightDispellableEffect):
   def __init__(self,input):
      super().__init__(input)
      self._immuneSpellIdFunc(input)
   
   def _immuneSpellIdFunc(self,input) :
      self.immuneSpellId = input.readInt()

   def resume(self):
      super().resume()
      print("immuneSpellId :",self.immuneSpellId)
