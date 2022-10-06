from tmp.messages.AbstractPartyMemberInFightMessage import AbstractPartyMemberInFightMessage
from tmp.types.MapCoordinatesExtended import MapCoordinatesExtended

class PartyMemberInStandardFightMessage(AbstractPartyMemberInFightMessage):
   def __init__(self,input):
      super().__init__(input)
      self.fightMap = MapCoordinatesExtended(input)

   def resume(self):
      super().resume()
      self.fightMap.resum()
