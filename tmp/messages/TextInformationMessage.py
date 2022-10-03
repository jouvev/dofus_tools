class TextInformationMessage:
   def __init__(self,input):
      self.parameters = []
      _val3 = None
      self._msgTypeFunc(input)
      self._msgIdFunc(input)
      _parametersLen = input.readUnsignedShort()
      for _i3 in range(0,_parametersLen):
         _val3 = input.readUTF()
         self.parameters.append(_val3)
   
   def _msgTypeFunc(self,input) :
      self.msgType = input.readByte()
      if(self.msgType < 0) :
         raise RuntimeError("Forbidden value (" + self.msgType + ") on element of TextInformationMessage.msgType.")
   
   def _msgIdFunc(self,input) :
      self.msgId = input.readVarUhShort()
      if(self.msgId < 0) :
         raise RuntimeError("Forbidden value (" + self.msgId + ") on element of TextInformationMessage.msgId.")