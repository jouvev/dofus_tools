class CurrentServerStatusUpdateMessage:
   def __init__(self,input):
      self._statusFunc(input)
   
   def _statusFunc(self,input) :
      self.status = input.readByte()
      if(self.status < 0) :
         raise RuntimeError("Forbidden value (" + self.status + ") on element of CurrentServerStatusUpdateMessage.status.")