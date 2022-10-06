from tmp.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyLeaveMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
