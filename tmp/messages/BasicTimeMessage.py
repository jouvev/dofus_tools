class BasicTimeMessage:
   def __init__(self,input):
      self._timestampFunc(input)
      self._timezoneOffsetFunc(input)
   
   def _timestampFunc(self,input) :
      self.timestamp = input.readDouble()
      if(self.timestamp < 0 or self.timestamp > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.timestamp) + ") on element of BasicTimeMessage.timestamp.")
   
   def _timezoneOffsetFunc(self,input) :
      self.timezoneOffset = input.readShort()

   def resume(self):
      print("timestamp :",self.timestamp)
      print("timezoneOffset :",self.timezoneOffset)
