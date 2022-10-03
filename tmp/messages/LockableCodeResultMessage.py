class LockableCodeResultMessage:
   def __init__(self,input):
      self._resultFunc(input)
   
   def _resultFunc(self,input) :
      self.result = input.readByte()
      if(self.result < 0) :
         raise RuntimeError("Forbidden value (" + self.result + ") on element of LockableCodeResultMessage.result.")