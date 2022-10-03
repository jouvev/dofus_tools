class ObjectDeleteMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectUID + ") on element of ObjectDeleteMessage.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ObjectDeleteMessage.quantity.")