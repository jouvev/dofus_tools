class ContactLookErrorMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readVarUhInt()
      if(self.requestId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.requestId) + ") on element of ContactLookErrorMessage.requestId.")

   def resume(self):
      print("requestId :",self.requestId)
