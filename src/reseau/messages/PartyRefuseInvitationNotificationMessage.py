from src.reseau.messages.AbstractPartyEventMessage import AbstractPartyEventMessage

class PartyRefuseInvitationNotificationMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self._guestIdFunc(input)
   
   def _guestIdFunc(self,input) :
      self.guestId = input.readVarUhLong()
      if(self.guestId < 0 or self.guestId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.guestId) + ") on element of PartyRefuseInvitationNotificationMessage.guestId.")

   def resume(self):
      super().resume()
      print("guestId :",self.guestId)
