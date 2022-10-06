from tmp.types.SpellForPreset import SpellForPreset
from tmp.types.Preset import Preset

class SpellsPreset(Preset):
   def __init__(self,input):
      self.spells = []
      _item1 = None
      super().__init__(input)
      _spellsLen = input.readUnsignedShort()
      for _i1 in range(0,_spellsLen):
         _item1 = SpellForPreset(input)
         self.spells.append(_item1)

   def resume(self):
      super().resume()
      for e in self.spells:
         e.resume()
