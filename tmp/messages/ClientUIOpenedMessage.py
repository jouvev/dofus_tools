class ClientUIOpenedMessage:
   def __init__(self,input):
      self._typeFunc(input)
   
   def _typeFunc(self,input) :
      self.type = input.readByte()
      if(self.type < 0) :
         raise RuntimeError("Forbidden value (" + self.type + ") on element of ClientUIOpenedMessage.type.")