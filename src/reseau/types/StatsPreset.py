from src.reseau.types.SimpleCharacterCharacteristicForPreset import SimpleCharacterCharacteristicForPreset
from src.reseau.types.Preset import Preset

class StatsPreset(Preset):
   def __init__(self,input):
      self.stats = []
      _item1 = None
      super().__init__(input)
      _statsLen = input.readUnsignedShort()
      for _i1 in range(0,_statsLen):
         _item1 = SimpleCharacterCharacteristicForPreset(input)
         self.stats.append(_item1)

   def resume(self):
      super().resume()
      for e in self.stats:
         e.resume()
