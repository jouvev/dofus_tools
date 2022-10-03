class BasicPongMessage:
   def __init__(self,input):
      self._quietFunc(input)
   
   def _quietFunc(self,input) :
      self.quiet = input.readBoolean()