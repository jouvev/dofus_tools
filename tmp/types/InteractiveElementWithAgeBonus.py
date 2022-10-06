from tmp.types.InteractiveElement import InteractiveElement

class InteractiveElementWithAgeBonus(InteractiveElement):
   def __init__(self,input):
      super().__init__(input)
      self._ageBonusFunc(input)
   
   def _ageBonusFunc(self,input) :
      self.ageBonus = input.readShort()
      if(self.ageBonus < -1 or self.ageBonus > 1000) :
         raise RuntimeError("Forbidden value (" + str(self.ageBonus) + ") on element of InteractiveElementWithAgeBonus.ageBonus.")

   def resume(self):
      super().resume()
      print("ageBonus :",self.ageBonus)
