class AccountLoggingKickedMessage:
   def __init__(self,input):
      self._daysFunc(input)
      self._hoursFunc(input)
      self._minutesFunc(input)
   
   def _daysFunc(self,input) :
      self.days = input.readVarUhShort()
      if(self.days < 0) :
         raise RuntimeError("Forbidden value (" + self.days + ") on element of AccountLoggingKickedMessage.days.")
   
   def _hoursFunc(self,input) :
      self.hours = input.readByte()
      if(self.hours < 0) :
         raise RuntimeError("Forbidden value (" + self.hours + ") on element of AccountLoggingKickedMessage.hours.")
   
   def _minutesFunc(self,input) :
      self.minutes = input.readByte()
      if(self.minutes < 0) :
         raise RuntimeError("Forbidden value (" + self.minutes + ") on element of AccountLoggingKickedMessage.minutes.")