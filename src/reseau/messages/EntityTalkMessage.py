class EntityTalkMessage:
   def __init__(self,input):
      self.parameters = []
      _val3 = None
      self._entityIdFunc(input)
      self._textIdFunc(input)
      _parametersLen = input.readUnsignedShort()
      for _i3 in range(0,_parametersLen):
         _val3 = input.readUTF()
         self.parameters.append(_val3)
   
   def _entityIdFunc(self,input) :
      self.entityId = input.readDouble()
      if(self.entityId < -9007199254740992 or self.entityId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.entityId) + ") on element of EntityTalkMessage.entityId.")
   
   def _textIdFunc(self,input) :
      self.textId = input.readVarUhShort()
      if(self.textId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.textId) + ") on element of EntityTalkMessage.textId.")

   def resume(self):
      print("entityId :",self.entityId)
      print("textId :",self.textId)
      print("parameters :",self.parameters)
