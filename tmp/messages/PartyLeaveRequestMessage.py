from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
class PartyLeaveRequestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)