class ContactLookRequestMessage:
   def __init__(self,input):
      self._requestIdFunc(input)
      self._contactTypeFunc(input)
   
   def _requestIdFunc(self,input) :
      self.requestId = input.readUnsignedByte()
      if(self.requestId < 0 or self.requestId > 255) :
         raise RuntimeError("Forbidden value (" + self.requestId + ") on element of ContactLookRequestMessage.requestId.")
   
   def _contactTypeFunc(self,input) :
      self.contactType = input.readByte()
      if(self.contactType < 0) :
         raise RuntimeError("Forbidden value (" + self.contactType + ") on element of ContactLookRequestMessage.contactType.")