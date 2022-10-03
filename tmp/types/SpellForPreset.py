class SpellForPreset:
   def __init__(self,input):
      self.shortcuts = []
      _val2 = 0
      self._spellIdFunc(input)
      _shortcutsLen = input.readUnsignedShort()
      for _i2 in range(0,_shortcutsLen):
         _val2 = input.readShort()
         self.shortcuts.append(_val2)
   
   def _spellIdFunc(self,input) :
      self.spellId = input.readVarUhShort()
      if(self.spellId < 0) :
         raise RuntimeError("Forbidden value (" + self.spellId + ") on element of SpellForPreset.spellId.")