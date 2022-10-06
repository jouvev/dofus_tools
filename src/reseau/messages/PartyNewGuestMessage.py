from src.reseau.messages.AbstractPartyEventMessage import AbstractPartyEventMessage
from src.reseau.types.PartyGuestInformations import PartyGuestInformations

class PartyNewGuestMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self.guest = PartyGuestInformations(input)

   def resume(self):
      super().resume()
      self.guest.resum()
