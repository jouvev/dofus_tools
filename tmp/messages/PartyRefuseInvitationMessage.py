from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyRefuseInvitationMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
