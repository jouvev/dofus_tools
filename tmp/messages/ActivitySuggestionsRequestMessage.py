class ActivitySuggestionsRequestMessage:
   def __init__(self,input):
      self._minLevelFunc(input)
      self._maxLevelFunc(input)
      self._areaIdFunc(input)
      self._activityCategoryIdFunc(input)
      self._nbCardsFunc(input)
   
   def _minLevelFunc(self,input) :
      self.minLevel = input.readVarUhShort()
      if(self.minLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of ActivitySuggestionsRequestMessage.minLevel.")
   
   def _maxLevelFunc(self,input) :
      self.maxLevel = input.readVarUhShort()
      if(self.maxLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.maxLevel) + ") on element of ActivitySuggestionsRequestMessage.maxLevel.")
   
   def _areaIdFunc(self,input) :
      self.areaId = input.readVarUhShort()
      if(self.areaId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.areaId) + ") on element of ActivitySuggestionsRequestMessage.areaId.")
   
   def _activityCategoryIdFunc(self,input) :
      self.activityCategoryId = input.readVarUhShort()
      if(self.activityCategoryId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.activityCategoryId) + ") on element of ActivitySuggestionsRequestMessage.activityCategoryId.")
   
   def _nbCardsFunc(self,input) :
      self.nbCards = input.readUnsignedShort()
      if(self.nbCards < 0 or self.nbCards > 65535) :
         raise RuntimeError("Forbidden value (" + str(self.nbCards) + ") on element of ActivitySuggestionsRequestMessage.nbCards.")

   def resume(self):
      print("minLevel :",self.minLevel)
      print("maxLevel :",self.maxLevel)
      print("areaId :",self.areaId)
      print("activityCategoryId :",self.activityCategoryId)
      print("nbCards :",self.nbCards)
