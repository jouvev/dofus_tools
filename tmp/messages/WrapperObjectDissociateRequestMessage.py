class WrapperObjectDissociateRequestMessage:
   def __init__(self,input):
      self._hostUIDFunc(input)
      self._hostPosFunc(input)
   
   def _hostUIDFunc(self,input) :
      self.hostUID = input.readVarUhInt()
      if(self.hostUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.hostUID) + ") on element of WrapperObjectDissociateRequestMessage.hostUID.")
   
   def _hostPosFunc(self,input) :
      self.hostPos = input.readUnsignedByte()
      if(self.hostPos < 0 or self.hostPos > 255) :
         raise RuntimeError("Forbidden value (" + str(self.hostPos) + ") on element of WrapperObjectDissociateRequestMessage.hostPos.")

   def resume(self):
      print("hostUID :",self.hostUID)
      print("hostPos :",self.hostPos)
