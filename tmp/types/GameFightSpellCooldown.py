class GameFightSpellCooldown:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._cooldownFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readInt()
   
   def _cooldownFunc(self,input) :
      self.cooldown = input.readByte()
      if(self.cooldown < 0) :
         raise RuntimeError("Forbidden value (" + str(self.cooldown) + ") on element of GameFightSpellCooldown.cooldown.")

   def resume(self):
      print("spellId :",self.spellId)
      print("cooldown :",self.cooldown)
