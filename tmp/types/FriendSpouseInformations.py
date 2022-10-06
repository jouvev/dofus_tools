from tmp.types.EntityLook import EntityLook
from tmp.types.GuildInformations import GuildInformations

class FriendSpouseInformations:
   def __init__(self,input):
      self._spouseAccountIdFunc(input)
      self._spouseIdFunc(input)
      self._spouseNameFunc(input)
      self._spouseLevelFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self.spouseEntityLook = EntityLook(input)
      self.guildInfo = GuildInformations(input)
      self._alignmentSideFunc(input)
   
   def _spouseAccountIdFunc(self,input) :
      self.spouseAccountId = input.readInt()
      if(self.spouseAccountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spouseAccountId) + ") on element of FriendSpouseInformations.spouseAccountId.")
   
   def _spouseIdFunc(self,input) :
      self.spouseId = input.readVarUhLong()
      if(self.spouseId < 0 or self.spouseId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.spouseId) + ") on element of FriendSpouseInformations.spouseId.")
   
   def _spouseNameFunc(self,input) :
      self.spouseName = input.readUTF()
   
   def _spouseLevelFunc(self,input) :
      self.spouseLevel = input.readVarUhShort()
      if(self.spouseLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.spouseLevel) + ") on element of FriendSpouseInformations.spouseLevel.")
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
   
   def _sexFunc(self,input) :
      self.sex = input.readByte()
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()

   def resume(self):
      print("spouseAccountId :",self.spouseAccountId)
      print("spouseId :",self.spouseId)
      print("spouseName :",self.spouseName)
      print("spouseLevel :",self.spouseLevel)
      print("breed :",self.breed)
      print("sex :",self.sex)
      print("alignmentSide :",self.alignmentSide)
      self.spouseEntityLook.resum()
      self.guildInfo.resum()
