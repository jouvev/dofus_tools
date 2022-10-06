class LivingObjectMessageRequestMessage:
   def __init__(self,input):
      self.parameters = []
      _val2 = None
      self._msgIdFunc(input)
      _parametersLen = input.readUnsignedShort()
      for _i2 in range(0,_parametersLen):
         _val2 = input.readUTF()
         self.parameters.append(_val2)
      self._livingObjectFunc(input)
   
   def _msgIdFunc(self,input) :
      self.msgId = input.readVarUhShort()
      if(self.msgId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.msgId) + ") on element of LivingObjectMessageRequestMessage.msgId.")
   
   def _livingObjectFunc(self,input) :
      self.livingObject = input.readVarUhInt()
      if(self.livingObject < 0) :
         raise RuntimeError("Forbidden value (" + str(self.livingObject) + ") on element of LivingObjectMessageRequestMessage.livingObject.")

   def resume(self):
      print("msgId :",self.msgId)
      print("livingObject :",self.livingObject)
      print("parameters :",self.parameters)
