class SequenceNumberMessage:
   def __init__(self,input):
      self._numberFunc(input)
   
   def _numberFunc(self,input) :
      self.number = input.readUnsignedShort()
      if(self.number < 0 or self.number > 65535) :
         raise RuntimeError("Forbidden value (" + self.number + ") on element of SequenceNumberMessage.number.")