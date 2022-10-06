from src.reseau.types.ObjectEffectInteger import ObjectEffectInteger

class BreachBonusMessage:
   def __init__(self,input):
      self.bonus = ObjectEffectInteger(input)

   def resume(self):
      self.bonus.resum()
