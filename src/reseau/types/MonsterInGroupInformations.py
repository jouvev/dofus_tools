from src.reseau.types.EntityLook import EntityLook
from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations

class MonsterInGroupInformations(MonsterInGroupLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self.look = EntityLook(input)

   def resume(self):
      super().resume()
      self.look.resume()
