class UpdateSelfAgressableStatusMessage:
   def __init__(self,input):
      self._statusFunc(input)
      self._probationTimeFunc(input)
   
   def _statusFunc(self,input) :
      self.status = input.readByte()
      if(self.status < 0) :
         raise RuntimeError("Forbidden value (" + self.status + ") on element of UpdateSelfAgressableStatusMessage.status.")
   
   def _probationTimeFunc(self,input) :
      self.probationTime = input.readInt()
      if(self.probationTime < 0) :
         raise RuntimeError("Forbidden value (" + self.probationTime + ") on element of UpdateSelfAgressableStatusMessage.probationTime.")