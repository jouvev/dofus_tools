from src.reseau.types.Shortcut import Shortcut

class ShortcutSpell(Shortcut):
   def __init__(self,input):
      super().__init__(input)
      self._spellIdFunc(input)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spellId) + ") on element of ShortcutSpell.spellId.")

   def resume(self):
      super().resume()
      print("spellId :",self.spellId)
