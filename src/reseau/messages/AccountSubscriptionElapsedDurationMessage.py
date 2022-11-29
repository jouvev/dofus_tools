class AccountSubscriptionElapsedDurationMessage:
   def __init__(self,input):
      self._subscriptionElapsedDurationFunc(input)
   
   def _subscriptionElapsedDurationFunc(self,input) :
      self.subscriptionElapsedDuration = input.readDouble()
      if(self.subscriptionElapsedDuration < 0 or self.subscriptionElapsedDuration > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.subscriptionElapsedDuration) + ") on element of AccountSubscriptionElapsedDurationMessage.subscriptionElapsedDuration.")

   def resume(self):
      print("subscriptionElapsedDuration :",self.subscriptionElapsedDuration)
