class GameContextCreateMessage:
   def __init__(self,input):
      self._contextFunc(input)
   
   def _contextFunc(self,input) :
      self.context = input.readByte()
      if(self.context < 0) :
         raise RuntimeError("Forbidden value (" + self.context + ") on element of GameContextCreateMessage.context.")