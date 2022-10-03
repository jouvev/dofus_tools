class SystemMessageDisplayMessage:
   def __init__(self,input):
      self.parameters = []
      _val3 = None
      self._hangUpFunc(input)
      self._msgIdFunc(input)
      _parametersLen = input.readUnsignedShort()
      for _i3 in range(0,_parametersLen):
         _val3 = input.readUTF()
         self.parameters.append(_val3)
   
   def _hangUpFunc(self,input) :
      self.hangUp = input.readBoolean()
   
   def _msgIdFunc(self,input) :
      self.msgId = input.readVarUhShort()
      if(self.msgId < 0) :
         raise RuntimeError("Forbidden value (" + self.msgId + ") on element of SystemMessageDisplayMessage.msgId.")