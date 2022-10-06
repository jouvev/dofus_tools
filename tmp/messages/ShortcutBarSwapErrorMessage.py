class ShortcutBarSwapErrorMessage:
   def __init__(self,input):
      self._errorFunc(input)
   
   def _errorFunc(self,input) :
      self.error = input.readByte()
      if(self.error < 0) :
         raise RuntimeError("Forbidden value (" + str(self.error) + ") on element of ShortcutBarSwapErrorMessage.error.")

   def resume(self):
      print("error :",self.error)
