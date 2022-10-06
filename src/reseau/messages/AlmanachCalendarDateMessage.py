class AlmanachCalendarDateMessage:
   def __init__(self,input):
      self._dateFunc(input)
   
   def _dateFunc(self,input) :
      self.date = input.readInt()

   def resume(self):
      print("date :",self.date)
