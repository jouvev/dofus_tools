from tmp.messages.PartyInvitationRequestMessage import PartyInvitationRequestMessage

class PartyInvitationArenaRequestMessage(PartyInvitationRequestMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
