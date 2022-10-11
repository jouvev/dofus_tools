from src.reseau.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from src.reseau.types.MapCoordinatesExtended import MapCoordinatesExtended

class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
   def __init__(self,input):
      super().__init__(input)
      self.fightMap = MapCoordinatesExtended(input)

   def resume(self):
      super().resume()
      self.fightMap.resume()
