class RefreshFollowedQuestsOrderRequestMessage:
   def __init__(self,input):
      self.quests = []
      _val1 = 0
      _questsLen = input.readUnsignedShort()
      for _i1 in range(0,_questsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of quests.")
         self.quests.append(_val1)