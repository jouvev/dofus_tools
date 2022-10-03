class ObjectDeletedMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ObjectDeletedMessage.objectUID.")