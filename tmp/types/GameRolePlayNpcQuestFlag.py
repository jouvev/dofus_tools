class GameRolePlayNpcQuestFlag:
   def __init__(self,input):
      self.questsToValidId = []
      self.questsToStartId = []
      _val1 = 0
      _val2 = 0
      _questsToValidIdLen = input.readUnsignedShort()
      for _i1 in range(0,_questsToValidIdLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of questsToValidId.")
         self.questsToValidId.append(_val1)
      _questsToStartIdLen = input.readUnsignedShort()
      for _i2 in range(0,_questsToStartIdLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of questsToStartId.")
         self.questsToStartId.append(_val2)