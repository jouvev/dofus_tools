from tmp.types.Shortcut import Shortcut
class ShortcutSpell(Shortcut):
   def __init__(self,input):
      super().__init__(input)
      self._spellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of ShortcutSpell.spellId.")