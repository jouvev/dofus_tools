class BreachExitResponseMessage:
   def __init__(self,input):
      self._exitedFunc(input)
   
   def _exitedFunc(self,input) :
      self.exited = input.readBoolean()

   def resume(self):
      print("exited :",self.exited)
