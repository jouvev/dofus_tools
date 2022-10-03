import tmp.TypesFactory as pf
from tmp.types.PlayerNote import PlayerNote
from tmp.types.CharacterMinimalInformations import CharacterMinimalInformations
class GuildMember(CharacterMinimalInformations):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._breedFunc(input)
      self._rankIdFunc(input)
      self._enrollmentDateFunc(input)
      self._givenExperienceFunc(input)
      self._experienceGivenPercentFunc(input)
      self._connectedFunc(input)
      self._alignmentSideFunc(input)
      self._hoursSinceLastConnectionFunc(input)
      self._moodSmileyIdFunc(input)
      self._accountIdFunc(input)
      self._achievementPointsFunc(input)
      _id13 = input.readUnsignedShort()
      self.status = pf.TypesFactory.get_instance_id(_id13,input)
      self.note = PlayerNote(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.sex = bool(bin(_box0)[2:].zfill(8)[0])
      self.havenBagShared = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
   
   def _rankIdFunc(self,input) :
      self.rankId = input.readVarUhInt()
      if(self.rankId < 0) :
         raise RuntimeError("Forbidden value (" + self.rankId + ") on element of GuildMember.rankId.")
   
   def _enrollmentDateFunc(self,input) :
      self.enrollmentDate = input.readDouble()
      if(self.enrollmentDate < -9007199254740992 or self.enrollmentDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.enrollmentDate + ") on element of GuildMember.enrollmentDate.")
   
   def _givenExperienceFunc(self,input) :
      self.givenExperience = input.readVarUhLong()
      if(self.givenExperience < 0 or self.givenExperience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.givenExperience + ") on element of GuildMember.givenExperience.")
   
   def _experienceGivenPercentFunc(self,input) :
      self.experienceGivenPercent = input.readByte()
      if(self.experienceGivenPercent < 0 or self.experienceGivenPercent > 100) :
         raise RuntimeError("Forbidden value (" + self.experienceGivenPercent + ") on element of GuildMember.experienceGivenPercent.")
   
   def _connectedFunc(self,input) :
      self.connected = input.readByte()
      if(self.connected < 0) :
         raise RuntimeError("Forbidden value (" + self.connected + ") on element of GuildMember.connected.")
   
   def _alignmentSideFunc(self,input) :
      self.alignmentSide = input.readByte()
   
   def _hoursSinceLastConnectionFunc(self,input) :
      self.hoursSinceLastConnection = input.readUnsignedShort()
      if(self.hoursSinceLastConnection < 0 or self.hoursSinceLastConnection > 65535) :
         raise RuntimeError("Forbidden value (" + self.hoursSinceLastConnection + ") on element of GuildMember.hoursSinceLastConnection.")
   
   def _moodSmileyIdFunc(self,input) :
      self.moodSmileyId = input.readVarUhShort()
      if(self.moodSmileyId < 0) :
         raise RuntimeError("Forbidden value (" + self.moodSmileyId + ") on element of GuildMember.moodSmileyId.")
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of GuildMember.accountId.")
   
   def _achievementPointsFunc(self,input) :
      self.achievementPoints = input.readInt()