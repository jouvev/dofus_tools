from tmp.messages.AbstractPartyMessage import AbstractPartyMessage
class PartyInvitationCancelledForGuestMessage(AbstractPartyMessage):
   def __init__(self,input):
      super().__init__(input)
      self._cancelerIdFunc(input)
   
   def _cancelerIdFunc(self,input) :
      self.cancelerId = input.readVarUhLong()
      if(self.cancelerId < 0 or self.cancelerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.cancelerId + ") on element of PartyInvitationCancelledForGuestMessage.cancelerId.")