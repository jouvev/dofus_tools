from tmp.types.EntityLook import EntityLook
from tmp.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
class MonsterInGroupInformations(MonsterInGroupLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self.look = EntityLook(input)