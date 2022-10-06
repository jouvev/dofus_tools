from src.reseau.messages.AbstractPartyMessage import AbstractPartyMessage

class PartyInvitationCancelledForGuestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._cancelerIdFunc(input)
   
   def _cancelerIdFunc(self,input) :
      self.cancelerId = input.readVarUhLong()
      if(self.cancelerId < 0 or self.cancelerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.cancelerId) + ") on element of PartyInvitationCancelledForGuestMessage.cancelerId.")

   def resume(self):
      super().resume()
      print("cancelerId :",self.cancelerId)
