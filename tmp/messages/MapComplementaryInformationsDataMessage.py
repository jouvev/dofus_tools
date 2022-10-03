import tmp.TypesFactory as pf
from tmp.types.StatedElement import StatedElement
from tmp.types.MapObstacle import MapObstacle
from tmp.types.FightCommonInformations import FightCommonInformations
from tmp.types.FightStartingPositions import FightStartingPositions
class MapComplementaryInformationsDataMessage:
   def __init__(self,input):
      self.houses = []
      self.actors = []
      self.interactiveElements = []
      self.statedElements = []
      self.obstacles = []
      self.fights = []
      _id3 = 0
      _item3 = None
      _id4 = 0
      _item4 = None
      _id5 = 0
      _item5 = None
      _item6 = None
      _item7 = None
      _item8 = None
      self._subAreaIdFunc(input)
      self._mapIdFunc(input)
      _housesLen = input.readUnsignedShort()
      for _i3 in range(0,_housesLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.houses.append(_item3)
      _actorsLen = input.readUnsignedShort()
      for _i4 in range(0,_actorsLen):
         _id4 = input.readUnsignedShort()
         _item4 = pf.TypesFactory.get_instance_id(_id4,input)
         self.actors.append(_item4)
      _interactiveElementsLen = input.readUnsignedShort()
      for _i5 in range(0,_interactiveElementsLen):
         _id5 = input.readUnsignedShort()
         _item5 = pf.TypesFactory.get_instance_id(_id5,input)
         self.interactiveElements.append(_item5)
      _statedElementsLen = input.readUnsignedShort()
      for _i6 in range(0,_statedElementsLen):
         _item6 = StatedElement(input)
         self.statedElements.append(_item6)
      _obstaclesLen = input.readUnsignedShort()
      for _i7 in range(0,_obstaclesLen):
         _item7 = MapObstacle(input)
         self.obstacles.append(_item7)
      _fightsLen = input.readUnsignedShort()
      for _i8 in range(0,_fightsLen):
         _item8 = FightCommonInformations(input)
         self.fights.append(_item8)
      self._hasAggressiveMonstersFunc(input)
      self.fightStartPositions = FightStartingPositions(input)
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of MapComplementaryInformationsDataMessage.subAreaId.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of MapComplementaryInformationsDataMessage.mapId.")
   
   def _hasAggressiveMonstersFunc(self,input) :
      self.hasAggressiveMonsters = input.readBoolean()