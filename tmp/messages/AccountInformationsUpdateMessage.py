class AccountInformationsUpdateMessage:
   def __init__(self,input):
      self._subscriptionEndDateFunc(input)
   
   def _subscriptionEndDateFunc(self,input) :
      self.subscriptionEndDate = input.readDouble()
      if(self.subscriptionEndDate < 0 or self.subscriptionEndDate > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.subscriptionEndDate + ") on element of AccountInformationsUpdateMessage.subscriptionEndDate.")