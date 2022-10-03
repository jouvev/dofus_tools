from tmp.types.MonsterBoosts import MonsterBoosts
from tmp.types.MonsterBoosts import MonsterBoosts
class GameRefreshMonsterBoostsMessage:
   def __init__(self,input):
      self.monsterBoosts = []
      self.familyBoosts = []
      _item1 = None
      _item2 = None
      _monsterBoostsLen = input.readUnsignedShort()
      for _i1 in range(0,_monsterBoostsLen):
         _item1 = MonsterBoosts(input)
         self.monsterBoosts.append(_item1)
      _familyBoostsLen = input.readUnsignedShort()
      for _i2 in range(0,_familyBoostsLen):
         _item2 = MonsterBoosts(input)
         self.familyBoosts.append(_item2)