class UpdateSelfAgressableStatusMessage:
   def __init__(self,input):
      self._statusFunc(input)
      self._probationTimeFunc(input)
   
   def _statusFunc(self,input) :
      self.status = input.readByte()
      if(self.status < 0) :
         raise RuntimeError("Forbidden value (" + str(self.status) + ") on element of UpdateSelfAgressableStatusMessage.status.")
   
   def _probationTimeFunc(self,input) :
      self.probationTime = input.readInt()
      if(self.probationTime < 0) :
         raise RuntimeError("Forbidden value (" + str(self.probationTime) + ") on element of UpdateSelfAgressableStatusMessage.probationTime.")

   def resume(self):
      print("status :",self.status)
      print("probationTime :",self.probationTime)
