from tmp.types.Shortcut import Shortcut

class ShortcutEntitiesPreset(Shortcut):
   def __init__(self,input):
      super().__init__(input)
      self._presetIdFunc(input)
   
   def _presetIdFunc(self,input) :
      self.presetId = input.readShort()

   def resume(self):
      super().resume()
      print("presetId :",self.presetId)
