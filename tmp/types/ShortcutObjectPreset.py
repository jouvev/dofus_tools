from tmp.types.ShortcutObject import ShortcutObject
class ShortcutObjectPreset(ShortcutObject):
   def __init__(self,input):
      super().__init__(input)
      self._presetIdFunc(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()