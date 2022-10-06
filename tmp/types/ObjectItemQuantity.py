from tmp.types.Item import Item

class ObjectItemQuantity(Item):
   def __init__(self,input):
      super().__init__(input)
      self._objectUIDFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ObjectItemQuantity.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ObjectItemQuantity.quantity.")

   def resume(self):
      super().resume()
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
