class SymbioticObjectAssociatedMessage:
   def __init__(self,input):
      self._hostUIDFunc(input)
   
   def _hostUIDFunc(self,input) :
      self.hostUID = input.readVarUhInt()
      if(self.hostUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.hostUID) + ") on element of SymbioticObjectAssociatedMessage.hostUID.")

   def resume(self):
      print("hostUID :",self.hostUID)
