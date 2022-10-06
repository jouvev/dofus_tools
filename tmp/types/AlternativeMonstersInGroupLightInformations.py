from tmp.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations

class AlternativeMonstersInGroupLightInformations:
   def __init__(self,input):
      self.monsters = []
      _item2 = None
      self._playerCountFunc(input)
      _monstersLen = input.readUnsignedShort()
      for _i2 in range(0,_monstersLen):
         _item2 = MonsterInGroupLightInformations(input)
         self.monsters.append(_item2)
   
   def _playerCountFunc(self,input) :
      self.playerCount = input.readInt()

   def resume(self):
      print("playerCount :",self.playerCount)
      for e in self.monsters:
         e.resume()
