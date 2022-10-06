class GuildSubmitApplicationMessage:
   def __init__(self,input):
      self._applyTextFunc(input)
      self._guildIdFunc(input)
      self._timeSpentFunc(input)
      self._filterLanguageFunc(input)
      self._filterAmbianceFunc(input)
      self._filterPlaytimeFunc(input)
      self._filterInterestFunc(input)
      self._filterMinMaxGuildLevelFunc(input)
      self._filterRecruitmentTypeFunc(input)
      self._filterMinMaxCharacterLevelFunc(input)
      self._filterMinMaxAchievementFunc(input)
      self._filterSearchNameFunc(input)
      self._filterLastSortFunc(input)
   
   def _applyTextFunc(self,input) :
      self.applyText = input.readUTF()
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of GuildSubmitApplicationMessage.guildId.")
   
   def _timeSpentFunc(self,input) :
      self.timeSpent = input.readVarUhInt()
      if(self.timeSpent < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timeSpent) + ") on element of GuildSubmitApplicationMessage.timeSpent.")
   
   def _filterLanguageFunc(self,input) :
      self.filterLanguage = input.readUTF()
   
   def _filterAmbianceFunc(self,input) :
      self.filterAmbiance = input.readUTF()
   
   def _filterPlaytimeFunc(self,input) :
      self.filterPlaytime = input.readUTF()
   
   def _filterInterestFunc(self,input) :
      self.filterInterest = input.readUTF()
   
   def _filterMinMaxGuildLevelFunc(self,input) :
      self.filterMinMaxGuildLevel = input.readUTF()
   
   def _filterRecruitmentTypeFunc(self,input) :
      self.filterRecruitmentType = input.readUTF()
   
   def _filterMinMaxCharacterLevelFunc(self,input) :
      self.filterMinMaxCharacterLevel = input.readUTF()
   
   def _filterMinMaxAchievementFunc(self,input) :
      self.filterMinMaxAchievement = input.readUTF()
   
   def _filterSearchNameFunc(self,input) :
      self.filterSearchName = input.readUTF()
   
   def _filterLastSortFunc(self,input) :
      self.filterLastSort = input.readUTF()

   def resume(self):
      print("applyText :",self.applyText)
      print("guildId :",self.guildId)
      print("timeSpent :",self.timeSpent)
      print("filterLanguage :",self.filterLanguage)
      print("filterAmbiance :",self.filterAmbiance)
      print("filterPlaytime :",self.filterPlaytime)
      print("filterInterest :",self.filterInterest)
      print("filterMinMaxGuildLevel :",self.filterMinMaxGuildLevel)
      print("filterRecruitmentType :",self.filterRecruitmentType)
      print("filterMinMaxCharacterLevel :",self.filterMinMaxCharacterLevel)
      print("filterMinMaxAchievement :",self.filterMinMaxAchievement)
      print("filterSearchName :",self.filterSearchName)
      print("filterLastSort :",self.filterLastSort)
