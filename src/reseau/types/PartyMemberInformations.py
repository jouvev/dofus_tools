import src.reseau.TypesFactory as pf
from src.reseau.types.CharacterBaseInformations import CharacterBaseInformations

class PartyMemberInformations(CharacterBaseInformations):
   def __init__(self,input):
      self.entities = []
      _id12 = 0
      _item12 = None
      super().__init__(input)
      self._lifePointsFunc(input)
      self._maxLifePointsFunc(input)
      self._prospectingFunc(input)
      self._regenRateFunc(input)
      self._initiativeFunc(input)
      self._alignmentSideFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      _id11 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id11,input)
      _entitiesLen = input.readUnsignedShort()
      for _i12 in range(0,_entitiesLen):
         _id12 = input.readUnsignedShort()
         _item12 = pf.TypesFactory.get_instance_id(_id12,input)
         self.entities.append(_item12)
   
   def _lifePointsFunc(self,input) :
      self.lifePoints = input.readVarUhInt()
      if(self.lifePoints < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lifePoints) + ") on element of PartyMemberInformations.lifePoints.")
   
   def _maxLifePointsFunc(self,input) :
      self.maxLifePoints = input.readVarUhInt()
      if(self.maxLifePoints < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxLifePoints) + ") on element of PartyMemberInformations.maxLifePoints.")
   
   def _prospectingFunc(self,input) :
      self.prospecting = input.readVarUhInt()
      if(self.prospecting < 0) :
         raise RuntimeError("Forbidden value (" + str(self.prospecting) + ") on element of PartyMemberInformations.prospecting.")
   
   def _regenRateFunc(self,input) :
      self.regenRate = input.readUnsignedByte()
      if(self.regenRate < 0 or self.regenRate > 255) :
         raise RuntimeError("Forbidden value (" + str(self.regenRate) + ") on element of PartyMemberInformations.regenRate.")
   
   def _initiativeFunc(self,input) :
      self.initiative = input.readVarUhInt()
      if(self.initiative < 0) :
         raise RuntimeError("Forbidden value (" + str(self.initiative) + ") on element of PartyMemberInformations.initiative.")
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PartyMemberInformations.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PartyMemberInformations.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of PartyMemberInformations.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PartyMemberInformations.subAreaId.")

   def resume(self):
      super().resume()
      print("lifePoints :",self.lifePoints)
      print("maxLifePoints :",self.maxLifePoints)
      print("prospecting :",self.prospecting)
      print("regenRate :",self.regenRate)
      print("initiative :",self.initiative)
      print("alignmentSide :",self.alignmentSide)
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("mapId :",self.mapId)
      print("subAreaId :",self.subAreaId)
      self.status.resume()
      for e in self.entities:
         e.resume()
