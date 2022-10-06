from tmp.types.FightResultAdditionalData import FightResultAdditionalData

class FightResultExperienceData(FightResultAdditionalData):
   def __init__(self,input):
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._experienceFunc(input)
      self._experienceLevelFloorFunc(input)
      self._experienceNextLevelFloorFunc(input)
      self._experienceFightDeltaFunc(input)
      self._experienceForGuildFunc(input)
      self._experienceForMountFunc(input)
      self._rerollExperienceMulFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.showExperience = bool(bin(_box0)[2:].zfill(8)[0])
      self.showExperienceLevelFloor = bool(bin(_box0)[2:].zfill(8)[1])
      self.showExperienceNextLevelFloor = bool(bin(_box0)[2:].zfill(8)[2])
      self.showExperienceFightDelta = bool(bin(_box0)[2:].zfill(8)[3])
      self.showExperienceForGuild = bool(bin(_box0)[2:].zfill(8)[4])
      self.showExperienceForMount = bool(bin(_box0)[2:].zfill(8)[5])
      self.isIncarnationExperience = bool(bin(_box0)[2:].zfill(8)[6])
   
   def _experienceFunc(self,input) :
      self.experience = input.readVarUhLong()
      if(self.experience < 0 or self.experience > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experience) + ") on element of FightResultExperienceData.experience.")
   
   def _experienceLevelFloorFunc(self,input) :
      self.experienceLevelFloor = input.readVarUhLong()
      if(self.experienceLevelFloor < 0 or self.experienceLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceLevelFloor) + ") on element of FightResultExperienceData.experienceLevelFloor.")
   
   def _experienceNextLevelFloorFunc(self,input) :
      self.experienceNextLevelFloor = input.readVarUhLong()
      if(self.experienceNextLevelFloor < 0 or self.experienceNextLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceNextLevelFloor) + ") on element of FightResultExperienceData.experienceNextLevelFloor.")
   
   def _experienceFightDeltaFunc(self,input) :
      self.experienceFightDelta = input.readVarUhLong()
      if(self.experienceFightDelta < 0 or self.experienceFightDelta > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceFightDelta) + ") on element of FightResultExperienceData.experienceFightDelta.")
   
   def _experienceForGuildFunc(self,input) :
      self.experienceForGuild = input.readVarUhLong()
      if(self.experienceForGuild < 0 or self.experienceForGuild > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceForGuild) + ") on element of FightResultExperienceData.experienceForGuild.")
   
   def _experienceForMountFunc(self,input) :
      self.experienceForMount = input.readVarUhLong()
      if(self.experienceForMount < 0 or self.experienceForMount > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.experienceForMount) + ") on element of FightResultExperienceData.experienceForMount.")
   
   def _rerollExperienceMulFunc(self,input) :
      self.rerollExperienceMul = input.readByte()
      if(self.rerollExperienceMul < 0) :
         raise RuntimeError("Forbidden value (" + str(self.rerollExperienceMul) + ") on element of FightResultExperienceData.rerollExperienceMul.")

   def resume(self):
      super().resume()
      print("experience :",self.experience)
      print("experienceLevelFloor :",self.experienceLevelFloor)
      print("experienceNextLevelFloor :",self.experienceNextLevelFloor)
      print("experienceFightDelta :",self.experienceFightDelta)
      print("experienceForGuild :",self.experienceForGuild)
      print("experienceForMount :",self.experienceForMount)
      print("rerollExperienceMul :",self.rerollExperienceMul)
