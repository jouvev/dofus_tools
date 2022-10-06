from tmp.messages.LeaveDialogMessage import LeaveDialogMessage

class ExchangeLeaveMessage(LeaveDialogMessage):
   def __init__(self,input):
      super().__init__(input)
      self._successFunc(input)
   
   def _successFunc(self,input) :
      self.success = input.readBoolean()

   def resume(self):
      super().resume()
      print("success :",self.success)
