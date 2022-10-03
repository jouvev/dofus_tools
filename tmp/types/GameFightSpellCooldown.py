class GameFightSpellCooldown:
   def __init__(self,input):
      self._spellIdFunc(input)
      self._cooldownFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readInt()
   
   def _cooldownFunc(self,input) :
      self.cooldown = input.readByte()
      if(self.cooldown < 0) :
         raise RuntimeError("Forbidden value (" + self.cooldown + ") on element of GameFightSpellCooldown.cooldown.")