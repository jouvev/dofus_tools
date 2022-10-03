from tmp.messages.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from tmp.types.GuildApplicationInformation import GuildApplicationInformation
class GuildListApplicationAnswerMessage(PaginationAnswerAbstractMessage):
   def __init__(self,input):
      self.applies = []
      _item1 = None
      super().__init__(input)
      _appliesLen = input.readUnsignedShort()
      for _i1 in range(0,_appliesLen):
         _item1 = GuildApplicationInformation(input)
         self.applies.append(_item1)