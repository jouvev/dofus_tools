from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
class PartyAcceptInvitationMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)