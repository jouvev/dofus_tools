from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
class PartyLocateMembersRequestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)