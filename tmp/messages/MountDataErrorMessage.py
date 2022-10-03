class MountDataErrorMessage:
   def __init__(self,input):
      self._reasonFunc(input)
   
   def _reasonFunc(self,input) :
      self.reason = input.readByte()
      if(self.reason < 0) :
         raise RuntimeError("Forbidden value (" + self.reason + ") on element of MountDataErrorMessage.reason.")