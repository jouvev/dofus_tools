class ObjectQuantityMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._quantityFunc(input)
      self._originFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectQuantityMessage.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectQuantityMessage.quantity.")
   
   def _originFunc(self,input) :
      self.origin = input.readByte()
      if(self.origin < 0) :
         raise RuntimeError("Forbidden value (" + str(self.origin) + ") on element of ObjectQuantityMessage.origin.")

   def resume(self):
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
      print("origin :",self.origin)
