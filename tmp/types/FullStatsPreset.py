from tmp.types.CharacterCharacteristicForPreset import CharacterCharacteristicForPreset
from tmp.types.Preset import Preset
class FullStatsPreset(Preset):
   def __init__(self,input):
      self.stats = []
      _item1 = None
      super().__init__(input)
      _statsLen = input.readUnsignedShort()
      for _i1 in range(0,_statsLen):
         _item1 = CharacterCharacteristicForPreset(input)
         self.stats.append(_item1)