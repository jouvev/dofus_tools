class CompassResetMessage:
   def __init__(self,input):
      self._typeFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + self.type + ") on element of CompassResetMessage.type.")