from src.reseau.messages.MapRunningFightDetailsMessage import MapRunningFightDetailsMessage
from src.reseau.types.NamedPartyTeam import NamedPartyTeam

class MapRunningFightDetailsExtendedMessage(MapRunningFightDetailsMessage):
   def __init__(self,input):
      self.namedPartyTeams = []
      _item1 = None
      super().__init__(input)
      _namedPartyTeamsLen = input.readUnsignedShort()
      for _i1 in range(0,_namedPartyTeamsLen):
         _item1 = NamedPartyTeam(input)
         self.namedPartyTeams.append(_item1)

   def resume(self):
      super().resume()
      for e in self.namedPartyTeams:
         e.resume()
