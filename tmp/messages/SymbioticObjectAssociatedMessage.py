class SymbioticObjectAssociatedMessage:
   def __init__(self,input):
      self._hostUIDFunc(input)
   
   def _hostUIDFunc(self,input) :
      self.hostUID = input.readVarUhInt()
      if(self.hostUID < 0) :
         raise RuntimeError("Forbidden value (" + self.hostUID + ") on element of SymbioticObjectAssociatedMessage.hostUID.")