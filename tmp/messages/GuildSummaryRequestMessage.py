from tmp.messages.PaginationRequestAbstractMessage import PaginationRequestAbstractMessage
class GuildSummaryRequestMessage(PaginationRequestAbstractMessage):
   def __init__(self,input):
      self.criterionFilter = []
      self.languagesFilter = []
      self.recruitmentTypeFilter = []
      _val3 = 0
      _val4 = 0
      _val5 = 0
      super().__init__(input)
      self.deserializeByteBoxes(input)
      self._nameFilterFunc(input)
      _criterionFilterLen = input.readUnsignedShort()
      for _i3 in range(0,_criterionFilterLen):
         _val3 = input.readVarUhInt()
         if(_val3 < 0) :
            raise RuntimeError("Forbidden value (" + _val3 + ") on elements of criterionFilter.")
         self.criterionFilter.append(_val3)
      _languagesFilterLen = input.readUnsignedShort()
      for _i4 in range(0,_languagesFilterLen):
         _val4 = input.readVarUhInt()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of languagesFilter.")
         self.languagesFilter.append(_val4)
      _recruitmentTypeFilterLen = input.readUnsignedShort()
      for _i5 in range(0,_recruitmentTypeFilterLen):
         _val5 = input.readByte()
         if(_val5 < 0) :
            raise RuntimeError("Forbidden value (" + _val5 + ") on elements of recruitmentTypeFilter.")
         self.recruitmentTypeFilter.append(_val5)
      self._minLevelFilterFunc(input)
      self._maxLevelFilterFunc(input)
      self._minPlayerLevelFilterFunc(input)
      self._maxPlayerLevelFilterFunc(input)
      self._minSuccessFilterFunc(input)
      self._maxSuccessFilterFunc(input)
      self._sortTypeFunc(input)
   
   def deserializeByteBoxes(self,input) :
      _box0 = input.readByte()
      self.hideFullFilter = bool(bin(_box0)[2:].zfill(8)[0])
      self.sortDescending = bool(bin(_box0)[2:].zfill(8)[1])
   
   def _nameFilterFunc(self,input) :
      self.nameFilter = input.readUTF()
   
   def _minLevelFilterFunc(self,input) :
      self.minLevelFilter = input.readShort()
      if(self.minLevelFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.minLevelFilter + ") on element of GuildSummaryRequestMessage.minLevelFilter.")
   
   def _maxLevelFilterFunc(self,input) :
      self.maxLevelFilter = input.readShort()
      if(self.maxLevelFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.maxLevelFilter + ") on element of GuildSummaryRequestMessage.maxLevelFilter.")
   
   def _minPlayerLevelFilterFunc(self,input) :
      self.minPlayerLevelFilter = input.readShort()
      if(self.minPlayerLevelFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.minPlayerLevelFilter + ") on element of GuildSummaryRequestMessage.minPlayerLevelFilter.")
   
   def _maxPlayerLevelFilterFunc(self,input) :
      self.maxPlayerLevelFilter = input.readShort()
      if(self.maxPlayerLevelFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.maxPlayerLevelFilter + ") on element of GuildSummaryRequestMessage.maxPlayerLevelFilter.")
   
   def _minSuccessFilterFunc(self,input) :
      self.minSuccessFilter = input.readVarUhInt()
      if(self.minSuccessFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.minSuccessFilter + ") on element of GuildSummaryRequestMessage.minSuccessFilter.")
   
   def _maxSuccessFilterFunc(self,input) :
      self.maxSuccessFilter = input.readVarUhInt()
      if(self.maxSuccessFilter < 0) :
         raise RuntimeError("Forbidden value (" + self.maxSuccessFilter + ") on element of GuildSummaryRequestMessage.maxSuccessFilter.")
   
   def _sortTypeFunc(self,input) :
      self.sortType = input.readByte()
      if(self.sortType < 0) :
         raise RuntimeError("Forbidden value (" + self.sortType + ") on element of GuildSummaryRequestMessage.sortType.")