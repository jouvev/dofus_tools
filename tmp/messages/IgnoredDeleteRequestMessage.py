class IgnoredDeleteRequestMessage:
   def __init__(self,input):
      self._accountIdFunc(input)
      self._sessionFunc(input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of IgnoredDeleteRequestMessage.accountId.")
   
   def _sessionFunc(self,input) :
      self.session = input.readBoolean()