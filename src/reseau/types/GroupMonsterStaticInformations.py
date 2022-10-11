from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from src.reseau.types.MonsterInGroupInformations import MonsterInGroupInformations

class GroupMonsterStaticInformations:
   def __init__(self,input):
      self.underlings = []
      _item2 = None
      self.mainCreatureLightInfos = MonsterInGroupLightInformations(input)
      _underlingsLen = input.readUnsignedShort()
      for _i2 in range(0,_underlingsLen):
         _item2 = MonsterInGroupInformations(input)
         self.underlings.append(_item2)

   def resume(self):
      self.mainCreatureLightInfos.resume()
      for e in self.underlings:
         e.resume()
