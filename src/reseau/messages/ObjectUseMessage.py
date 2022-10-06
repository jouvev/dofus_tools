class ObjectUseMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectUseMessage.objectUID.")

   def resume(self):
      print("objectUID :",self.objectUID)
