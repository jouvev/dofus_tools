import tmp.TypesFactory as pf
class QuestListMessage:
   def __init__(self,input):
      self.finishedQuestsIds = []
      self.finishedQuestsCounts = []
      self.activeQuests = []
      self.reinitDoneQuestsIds = []
      _val1 = 0
      _val2 = 0
      _id3 = 0
      _item3 = None
      _val4 = 0
      _finishedQuestsIdsLen = input.readUnsignedShort()
      for _i1 in range(0,_finishedQuestsIdsLen):
         _val1 = input.readVarUhShort()
         if(_val1 < 0) :
            raise RuntimeError("Forbidden value (" + _val1 + ") on elements of finishedQuestsIds.")
         self.finishedQuestsIds.append(_val1)
      _finishedQuestsCountsLen = input.readUnsignedShort()
      for _i2 in range(0,_finishedQuestsCountsLen):
         _val2 = input.readVarUhShort()
         if(_val2 < 0) :
            raise RuntimeError("Forbidden value (" + _val2 + ") on elements of finishedQuestsCounts.")
         self.finishedQuestsCounts.append(_val2)
      _activeQuestsLen = input.readUnsignedShort()
      for _i3 in range(0,_activeQuestsLen):
         _id3 = input.readUnsignedShort()
         _item3 = pf.TypesFactory.get_instance_id(_id3,input)
         self.activeQuests.append(_item3)
      _reinitDoneQuestsIdsLen = input.readUnsignedShort()
      for _i4 in range(0,_reinitDoneQuestsIdsLen):
         _val4 = input.readVarUhShort()
         if(_val4 < 0) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of reinitDoneQuestsIds.")
         self.reinitDoneQuestsIds.append(_val4)