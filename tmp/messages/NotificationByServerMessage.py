class NotificationByServerMessage:
   def __init__(self,input):
      self.parameters = []
      _val2 = None
      self._idFunc(input)
      _parametersLen = input.readUnsignedShort()
      for _i2 in range(0,_parametersLen):
         _val2 = input.readUTF()
         self.parameters.append(_val2)
      self._forceOpenFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhShort()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of NotificationByServerMessage.id.")
   
   def _forceOpenFunc(self,input) :
      self.forceOpen = input.readBoolean()