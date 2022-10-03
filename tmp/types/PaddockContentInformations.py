from tmp.types.MountInformationsForPaddock import MountInformationsForPaddock
from tmp.types.PaddockInformations import PaddockInformations
class PaddockContentInformations(PaddockInformations):
   def __init__(self,input):
      self.mountsInformations = []
      _item7 = None
      super().__init__(input)
      self._paddockIdFunc(input)
      self._worldXFunc(input)
      self._worldYFunc(input)
      self._mapIdFunc(input)
      self._subAreaIdFunc(input)
      self._abandonnedFunc(input)
      _mountsInformationsLen = input.readUnsignedShort()
      for _i7 in range(0,_mountsInformationsLen):
         _item7 = MountInformationsForPaddock(input)
         self.mountsInformations.append(_item7)
   
   def _paddockIdFunc(self,input) :
      self.paddockId = input.readDouble()
      if(self.paddockId < 0 or self.paddockId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.paddockId + ") on element of PaddockContentInformations.paddockId.")
   
   def _worldXFunc(self,input) :
      self.worldX = input.readShort()
      if(self.worldX < -255 or self.worldX > 255) :
         raise RuntimeError("Forbidden value (" + self.worldX + ") on element of PaddockContentInformations.worldX.")
   
   def _worldYFunc(self,input) :
      self.worldY = input.readShort()
      if(self.worldY < -255 or self.worldY > 255) :
         raise RuntimeError("Forbidden value (" + self.worldY + ") on element of PaddockContentInformations.worldY.")
   
   def _mapIdFunc(self,input) :
      self.mapId = input.readDouble()
      if(self.mapId < 0 or self.mapId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.mapId + ") on element of PaddockContentInformations.mapId.")
   
   def _subAreaIdFunc(self,input) :
      self.subAreaId = input.readVarUhShort()
      if(self.subAreaId < 0) :
         raise RuntimeError("Forbidden value (" + self.subAreaId + ") on element of PaddockContentInformations.subAreaId.")
   
   def _abandonnedFunc(self,input) :
      self.abandonned = input.readBoolean()