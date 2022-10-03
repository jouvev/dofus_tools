from tmp.messages.IdentificationFailedMessage import IdentificationFailedMessage
class IdentificationFailedBannedMessage(IdentificationFailedMessage):
   def __init__(self,input):
      super().__init__(input)
      self._banEndDateFunc(input)
   
   def _banEndDateFunc(self,input) :
      self.banEndDate = input.readDouble()
      if(self.banEndDate < 0 or self.banEndDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.banEndDate + ") on element of IdentificationFailedBannedMessage.banEndDate.")