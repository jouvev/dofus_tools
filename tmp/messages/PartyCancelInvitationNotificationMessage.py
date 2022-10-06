from tmp.messages.AbstractPartyEventMessage import AbstractPartyEventMessage

class PartyCancelInvitationNotificationMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self._cancelerIdFunc(input)
      self._guestIdFunc(input)
   
   def _cancelerIdFunc(self,input) :
      self.cancelerId = input.readVarUhLong()
      if(self.cancelerId < 0 or self.cancelerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.cancelerId) + ") on element of PartyCancelInvitationNotificationMessage.cancelerId.")
   
   def _guestIdFunc(self,input) :
      self.guestId = input.readVarUhLong()
      if(self.guestId < 0 or self.guestId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.guestId) + ") on element of PartyCancelInvitationNotificationMessage.guestId.")

   def resume(self):
      super().resume()
      print("cancelerId :",self.cancelerId)
      print("guestId :",self.guestId)
