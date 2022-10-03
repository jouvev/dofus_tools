from tmp.messages.AbstractPartyEventMessage import AbstractPartyEventMessage
from tmp.types.PartyGuestInformations import PartyGuestInformations
class PartyNewGuestMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self.guest = PartyGuestInformations(input)