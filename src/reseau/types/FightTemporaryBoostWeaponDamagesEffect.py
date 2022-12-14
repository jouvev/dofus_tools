from src.reseau.types.FightTemporaryBoostEffect import FightTemporaryBoostEffect

class FightTemporaryBoostWeaponDamagesEffect(FightTemporaryBoostEffect):
   def __init__(self,input):
      super().__init__(input)
      self._weaponTypeIdFunc(input)
   
   def _weaponTypeIdFunc(self,input) :
      self.weaponTypeId = input.readShort()

   def resume(self):
      super().resume()
      print("weaponTypeId :",self.weaponTypeId)
