from src.reseau.messages.PartyUpdateMessage import PartyUpdateMessage

class PartyNewMemberMessage(PartyUpdateMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
