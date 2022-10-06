from tmp.types.SpellsPreset import SpellsPreset
from tmp.types.SpellForPreset import SpellForPreset
from tmp.types.Preset import Preset

class ForgettableSpellsPreset(Preset):
   def __init__(self,input):
      self.forgettableSpells = []
      _item2 = None
      super().__init__(input)
      self.baseSpellsPreset = SpellsPreset(input)
      _forgettableSpellsLen = input.readUnsignedShort()
      for _i2 in range(0,_forgettableSpellsLen):
         _item2 = SpellForPreset(input)
         self.forgettableSpells.append(_item2)

   def resume(self):
      super().resume()
      self.baseSpellsPreset.resum()
      for e in self.forgettableSpells:
         e.resume()
