class ObjectDeleteMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectDeleteMessage.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectDeleteMessage.quantity.")

   def resume(self):
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
