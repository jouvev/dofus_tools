class ActivitySuggestionsMessage:
   def __init__(self,input):
      self.lockedActivitiesIds = []
      self.unlockedActivitiesIds = []
      _val1 = 0
      _val2 = 0
      _lockedActivitiesIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_lockedActivitiesIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of lockedActivitiesIds.")
         self.lockedActivitiesIds.append(_val1)
      _unlockedActivitiesIdsLen = input.readUnsignedShort()
      for _i2 in range(0,_unlockedActivitiesIdsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of unlockedActivitiesIds.")
         self.unlockedActivitiesIds.append(_val2)