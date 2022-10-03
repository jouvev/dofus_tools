from tmp.types.FriendSpouseInformations import FriendSpouseInformations
class FriendSpouseOnlineInformations(FriendSpouseInformations):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.inFight = bool(bin(_box0)[2:].zfill(8)[0])
      self.followSpouse = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of FriendSpouseOnlineInformations.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of FriendSpouseOnlineInformations.subAreaId.")