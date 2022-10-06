class BasicDateMessage:
   def __init__(self,input):
      self._dayFunc(input)
      self._monthFunc(input)
      self._yearFunc(input)
   
   def _dayFunc(self,input) :
      self.day = input.readByte()
      if(self.day < 0) :
         raise RuntimeError("Forbidden value (" + str(self.day) + ") on element of BasicDateMessage.day.")
   
   def _monthFunc(self,input) :
      self.month = input.readByte()
      if(self.month < 0) :
         raise RuntimeError("Forbidden value (" + str(self.month) + ") on element of BasicDateMessage.month.")
   
   def _yearFunc(self,input) :
      self.year = input.readShort()
      if(self.year < 0) :
         raise RuntimeError("Forbidden value (" + str(self.year) + ") on element of BasicDateMessage.year.")

   def resume(self):
      print("day :",self.day)
      print("month :",self.month)
      print("year :",self.year)
