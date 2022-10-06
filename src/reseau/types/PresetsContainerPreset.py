import src.reseau.TypesFactory as pf
from src.reseau.types.Preset import Preset

class PresetsContainerPreset(Preset):
   def __init__(self,input):
      self.presets = []
      _id1 = 0
      _item1 = None
      super().__init__(input)
      _presetsLen = input.readUnsignedShort()
      for _i1 in range(0,_presetsLen):
         _id1 = input.readUnsignedShort()
         _item1 = pf.TypesFactory.get_instance_id(_id1,input)
         self.presets.append(_item1)

   def resume(self):
      super().resume()
      for e in self.presets:
         e.resume()
