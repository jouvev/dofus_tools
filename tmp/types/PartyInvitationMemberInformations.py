from tmp.types.PartyEntityBaseInformation import PartyEntityBaseInformation
from tmp.types.CharacterBaseInformations import CharacterBaseInformations

class PartyInvitationMemberInformations(CharacterBaseInformations):
   def __init__(self,input):
      self.entities = []
      _item5 = None
      super().__init__(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      _entitiesLen = input.readUnsignedShort()
      for _i5 in range(0,_entitiesLen):
         _item5 = PartyEntityBaseInformation(input)
         self.entities.append(_item5)
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldX) + ") on element of PartyInvitationMemberInformations.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + str(self.worldY) + ") on element of PartyInvitationMemberInformations.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.mapId) + ") on element of PartyInvitationMemberInformations.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.subAreaId) + ") on element of PartyInvitationMemberInformations.subAreaId.")

   def resume(self):
      super().resume()
      print("worldX :",self.worldX)
      print("worldY :",self.worldY)
      print("mapId :",self.mapId)
      print("subAreaId :",self.subAreaId)
      for e in self.entities:
         e.resume()
