from src.reseau.messages.PaginationAnswerAbstractMessage import PaginationAnswerAbstractMessage
from src.reseau.types.AllianceFactSheetInformations import AllianceFactSheetInformations

class AllianceSummaryMessage(PaginationAnswerAbstractMessage):
   def __init__(self,input):
      self.alliances = []
      _item1 = None
      super().__init__(input)
      _alliancesLen = input.readUnsignedShort()
      for _i1 in range(0,_alliancesLen):
         _item1 = AllianceFactSheetInformations(input)
         self.alliances.append(_item1)

   def resume(self):
      super().resume()
      for e in self.alliances:
         e.resume()
