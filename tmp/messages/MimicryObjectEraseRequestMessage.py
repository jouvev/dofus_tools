class MimicryObjectEraseRequestMessage:
   def __init__(self,input):
      self._hostUIDFunc(input)
      self._hostPosFunc(input)
   
   def _hostUIDFunc(self,input) :
      self.hostUID = input.readVarUhInt()
      if(self.hostUID < 0) :
         raise RuntimeError("Forbidden value (" + self.hostUID + ") on element of MimicryObjectEraseRequestMessage.hostUID.")
   
   def _hostPosFunc(self,input) :
      self.hostPos = input.readUnsignedByte()
      if(self.hostPos < 0 or self.hostPos > 255) :
         raise RuntimeError("Forbidden value (" + self.hostPos + ") on element of MimicryObjectEraseRequestMessage.hostPos.")