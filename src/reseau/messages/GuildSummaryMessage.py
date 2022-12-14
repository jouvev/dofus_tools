from src.reseau.messages.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from src.reseau.types.GuildFactSheetInformations import GuildFactSheetInformations

class GuildSummaryMessage(PaginationAnswerAbstractMessage):
   def __init__(self,input):
      self.guilds = []
      _item1 = None
      super().__init__(input)
      _guildsLen = input.readUnsignedShort()
      for _i1 in range(0,_guildsLen):
         _item1 = GuildFactSheetInformations(input)
         self.guilds.append(_item1)

   def resume(self):
      super().resume()
      for e in self.guilds:
         e.resume()
