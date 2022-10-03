class CharacterExperienceGainMessage:
   def __init__(self,input):
      self._experienceCharacterFunc(input)
      self._experienceMountFunc(input)
      self._experienceGuildFunc(input)
      self._experienceIncarnationFunc(input)
   
   def _experienceCharacterFunc(self,input) :
      self.experienceCharacter = input.readVarUhLong()
      if(self.experienceCharacter < 0 or self.experienceCharacter > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceCharacter + ") on element of CharacterExperienceGainMessage.experienceCharacter.")
   
   def _experienceMountFunc(self,input) :
      self.experienceMount = input.readVarUhLong()
      if(self.experienceMount < 0 or self.experienceMount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceMount + ") on element of CharacterExperienceGainMessage.experienceMount.")
   
   def _experienceGuildFunc(self,input) :
      self.experienceGuild = input.readVarUhLong()
      if(self.experienceGuild < 0 or self.experienceGuild > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceGuild + ") on element of CharacterExperienceGainMessage.experienceGuild.")
   
   def _experienceIncarnationFunc(self,input) :
      self.experienceIncarnation = input.readVarUhLong()
      if(self.experienceIncarnation < 0 or self.experienceIncarnation > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.experienceIncarnation + ") on element of CharacterExperienceGainMessage.experienceIncarnation.")