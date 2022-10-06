from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
from tmp.types.PartyMemberGeoPosition import PartyMemberGeoPosition

class PartyLocateMembersMessage(AbstractPartyMessage):
   def __init__(self,input):
      self.geopositions = []
      _item1 = None
      super().__init__(input)
      _geopositionsLen = input.readUnsignedShort()
      for _i1 in range(0,_geopositionsLen):
         _item1 = PartyMemberGeoPosition(input)
         self.geopositions.append(_item1)

   def resume(self):
      super().resume()
      for e in self.geopositions:
         e.resume()
