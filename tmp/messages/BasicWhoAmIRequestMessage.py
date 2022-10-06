class BasicWhoAmIRequestMessage:
   def __init__(self,input):
      self._verboseFunc(input)
   
   def _verboseFunc(self,input) :
      self.verbose = input.readBoolean()

   def resume(self):
      print("verbose :",self.verbose)
