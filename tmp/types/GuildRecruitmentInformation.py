class GuildRecruitmentInformation:
   def __init__(self,input):
      self.selectedLanguages = []
      self.selectedCriterion = []
      _val5 = 0
      _val6 = 0
      self.deserializeByteBoxes(input)
      self._guildIdFunc(input)
      self._recruitmentTypeFunc(input)
      self._recruitmentTitleFunc(input)
      self._recruitmentTextFunc(input)
      _selectedLanguagesLen = input.readUnsignedShort()
      for _i5 in range(0,_selectedLanguagesLen):
         _val5 = input.readVarUhInt()
         if(_val5 < 0) :
            raise RuntimeError("Forbidden value (" + _val5 + ") on elements of selectedLanguages.")
         self.selectedLanguages.append(_val5)
      _selectedCriterionLen = input.readUnsignedShort()
      for _i6 in range(0,_selectedCriterionLen):
         _val6 = input.readVarUhInt()
         if(_val6 < 0) :
            raise RuntimeError("Forbidden value (" + _val6 + ") on elements of selectedCriterion.")
         self.selectedCriterion.append(_val6)
      self._minLevelFunc(input)
      self._minSuccessFunc(input)
      self._lastEditPlayerNameFunc(input)
      self._lastEditDateFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.minLevelFacultative = bool(bin(_box0)[2:].zfill(8)[0])
      self.minSuccessFacultative = bool(bin(_box0)[2:].zfill(8)[1])
      self.invalidatedByModeration = bool(bin(_box0)[2:].zfill(8)[2])
      self.recruitmentAutoLocked = bool(bin(_box0)[2:].zfill(8)[3])
   
   def _guildIdFunc(self,input) :
      self.guildId = input.readVarUhInt()
      if(self.guildId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.guildId) + ") on element of GuildRecruitmentInformation.guildId.")
   
   def _recruitmentTypeFunc(self,input) :
      self.recruitmentType = input.readByte()
      if(self.recruitmentType < 0) :
         raise RuntimeError("Forbidden value (" + str(self.recruitmentType) + ") on element of GuildRecruitmentInformation.recruitmentType.")
   
   def _recruitmentTitleFunc(self,input) :
      self.recruitmentTitle = input.readUTF()
   
   def _recruitmentTextFunc(self,input) :
      self.recruitmentText = input.readUTF()
   
   def _minLevelFunc(self,input) :
      self.minLevel = input.readShort()
      if(self.minLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of GuildRecruitmentInformation.minLevel.")
   
   def _minSuccessFunc(self,input) :
      self.minSuccess = input.readVarUhInt()
      if(self.minSuccess < 0) :
         raise RuntimeError("Forbidden value (" + str(self.minSuccess) + ") on element of GuildRecruitmentInformation.minSuccess.")
   
   def _lastEditPlayerNameFunc(self,input) :
      self.lastEditPlayerName = input.readUTF()
   
   def _lastEditDateFunc(self,input) :
      self.lastEditDate = input.readDouble()
      if(self.lastEditDate < -9007199254740992 or self.lastEditDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.lastEditDate) + ") on element of GuildRecruitmentInformation.lastEditDate.")

   def resume(self):
      print("guildId :",self.guildId)
      print("recruitmentType :",self.recruitmentType)
      print("recruitmentTitle :",self.recruitmentTitle)
      print("recruitmentText :",self.recruitmentText)
      print("minLevel :",self.minLevel)
      print("minSuccess :",self.minSuccess)
      print("lastEditPlayerName :",self.lastEditPlayerName)
      print("lastEditDate :",self.lastEditDate)
      print("selectedLanguages :",self.selectedLanguages)
      print("selectedCriterion :",self.selectedCriterion)
