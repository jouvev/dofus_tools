class LoginQueueStatusMessage:
   def __init__(self,input):
      self._positionFunc(input)
      self._totalFunc(input)
   
   def _positionFunc(self,input) :
      self.position = input.readUnsignedShort()
      if(self.position < 0 or self.position > 65535) :
         raise RuntimeError("Forbidden value (" + self.position + ") on element of LoginQueueStatusMessage.position.")
   
   def _totalFunc(self,input) :
      self.total = input.readUnsignedShort()
      if(self.total < 0 or self.total > 65535) :
         raise RuntimeError("Forbidden value (" + self.total + ") on element of LoginQueueStatusMessage.total.")