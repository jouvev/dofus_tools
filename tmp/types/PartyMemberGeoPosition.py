class PartyMemberGeoPosition:
   def __init__(self,input):
      self._memberIdFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readInt()
      if(self.memberId < 0) :
         raise RuntimeError("Forbidden value (" + self.memberId + ") on element of PartyMemberGeoPosition.memberId.")
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of PartyMemberGeoPosition.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of PartyMemberGeoPosition.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of PartyMemberGeoPosition.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PartyMemberGeoPosition.subAreaId.")