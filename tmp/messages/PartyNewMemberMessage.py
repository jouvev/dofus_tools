from tmp.messages.PartyUpdateMessage import PartyUpdateMessage
class PartyNewMemberMessage(PartyUpdateMessage):
   def __init__(self,input):
      super().__init__(input)