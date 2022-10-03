from tmp.types.AlternativeMonstersInGroupLightInformations import AlternativeMonstersInGroupLightInformations
from tmp.types.GroupMonsterStaticInformations import GroupMonsterStaticInformations
class GroupMonsterStaticInformationsWithAlternatives(GroupMonsterStaticInformations):
   def __init__(self,input):
      self.alternatives = []
      _item1 = None
      super().__init__(input)
      _alternativesLen = input.readUnsignedShort()
      for _i1 in range(0,_alternativesLen):
         _item1 = AlternativeMonstersInGroupLightInformations(input)
         self.alternatives.append(_item1)