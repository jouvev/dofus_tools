from tmp.types.QuestActiveDetailedInformations import QuestActiveDetailedInformations
class FollowedQuestsMessage:
   def __init__(self,input):
      self.quests = []
      _item1 = None
      _questsLen = input.readUnsignedShort()
      for _i1 in range(0,_questsLen):
         _item1 = QuestActiveDetailedInformations(input)
         self.quests.append(_item1)