class ContactLookErrorMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readVarUhInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + self.requestId + ") on element of ContactLookErrorMessage.requestId.")