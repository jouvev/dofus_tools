from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations
from src.reseau.types.MonsterInGroupLightInformations import MonsterInGroupLightInformations

class BreachBranch:
   def __init__(self,input):
      self.bosses = []
      self.monsters = []
      _item3 = None
      _item7 = None
      self._roomFunc(input)
      self._elementFunc(input)
      _bossesLen = input.readUnsignedShort()
      for _i3 in range(0,_bossesLen):
         _item3 = MonsterInGroupLightInformations(input)
         self.bosses.append(_item3)
      self._mapFunc(input)
      self._scoreFunc(input)
      self._relativeScoreFunc(input)
      _monstersLen = input.readUnsignedShort()
      for _i7 in range(0,_monstersLen):
         _item7 = MonsterInGroupLightInformations(input)
         self.monsters.append(_item7)
   
   def _roomFunc(self,input) :
      self.room = input.readByte()
      if(self.room < 0) :
         raise RuntimeError("Forbidden value (" + str(self.room) + ") on element of BreachBranch.room.")
   
   def _elementFunc(self,input) :
      self.element = input.readInt()
      if(self.element < 0) :
         raise RuntimeError("Forbidden value (" + str(self.element) + ") on element of BreachBranch.element.")
   
   def _mapFunc(self,input) :
      self.map = input.readDouble()
      if(self.map < 0 or self.map > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.map) + ") on element of BreachBranch.map.")
   
   def _scoreFunc(self,input) :
      self.score = input.readShort()
   
   def _relativeScoreFunc(self,input) :
      self.relativeScore = input.readShort()

   def resume(self):
      print("room :",self.room)
      print("element :",self.element)
      print("map :",self.map)
      print("score :",self.score)
      print("relativeScore :",self.relativeScore)
      for e in self.bosses:
         e.resume()
      for e in self.monsters:
         e.resume()
