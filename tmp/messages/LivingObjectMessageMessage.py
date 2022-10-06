class LivingObjectMessageMessage:
   def __init__(self,input):
      self._msgIdFunc(input)
      self._timeStampFunc(input)
      self._ownerFunc(input)
      self._objectGenericIdFunc(input)
   
   def _msgIdFunc(self,input) :
      self.msgId = input.readVarUhShort()
      if(self.msgId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.msgId) + ") on element of LivingObjectMessageMessage.msgId.")
   
   def _timeStampFunc(self,input) :
      self.timeStamp = input.readInt()
      if(self.timeStamp < 0) :
         raise RuntimeError("Forbidden value (" + str(self.timeStamp) + ") on element of LivingObjectMessageMessage.timeStamp.")
   
   def _ownerFunc(self,input) :
      self.owner = input.readUTF()
   
   def _objectGenericIdFunc(self,input) :
      self.objectGenericId = input.readVarUhInt()
      if(self.objectGenericId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectGenericId) + ") on element of LivingObjectMessageMessage.objectGenericId.")

   def resume(self):
      print("msgId :",self.msgId)
      print("timeStamp :",self.timeStamp)
      print("owner :",self.owner)
      print("objectGenericId :",self.objectGenericId)
