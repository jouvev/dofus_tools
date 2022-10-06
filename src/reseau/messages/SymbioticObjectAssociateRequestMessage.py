class SymbioticObjectAssociateRequestMessage:
   def __init__(self,input):
      self._symbioteUIDFunc(input)
      self._symbiotePosFunc(input)
      self._hostUIDFunc(input)
      self._hostPosFunc(input)
   
   def _symbioteUIDFunc(self,input) :
      self.symbioteUID = input.readVarUhInt()
      if(self.symbioteUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.symbioteUID) + ") on element of SymbioticObjectAssociateRequestMessage.symbioteUID.")
   
   def _symbiotePosFunc(self,input) :
      self.symbiotePos = input.readUnsignedByte()
      if(self.symbiotePos < 0 or self.symbiotePos > 255) :
         raise RuntimeError("Forbidden value (" + str(self.symbiotePos) + ") on element of SymbioticObjectAssociateRequestMessage.symbiotePos.")
   
   def _hostUIDFunc(self,input) :
      self.hostUID = input.readVarUhInt()
      if(self.hostUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.hostUID) + ") on element of SymbioticObjectAssociateRequestMessage.hostUID.")
   
   def _hostPosFunc(self,input) :
      self.hostPos = input.readUnsignedByte()
      if(self.hostPos < 0 or self.hostPos > 255) :
         raise RuntimeError("Forbidden value (" + str(self.hostPos) + ") on element of SymbioticObjectAssociateRequestMessage.hostPos.")

   def resume(self):
      print("symbioteUID :",self.symbioteUID)
      print("symbiotePos :",self.symbiotePos)
      print("hostUID :",self.hostUID)
      print("hostPos :",self.hostPos)
