from tmp.types.Item import Item
class ObjectItemGenericQuantity(Item):
   def __init__(self,input):
      super().__init__(input)
      self._objectGIDFunc(input)
      self._quantityFunc(input)
   
   def _objectGIDFunc(self,input) :
      self.objectGID = input.readVarUhInt()
      if(self.objectGID < 0) :
         raise RuntimeError("Forbidden value (" + self.objectGID + ") on element of ObjectItemGenericQuantity.objectGID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ObjectItemGenericQuantity.quantity.")