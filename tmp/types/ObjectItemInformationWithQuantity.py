from tmp.types.ObjectItemMinimalInformation import ObjectItemMinimalInformation
class ObjectItemInformationWithQuantity(ObjectItemMinimalInformation):
   def __init__(self,input):
      super().__init__(input)
      self._quantityFunc(input)
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhInt()
      if(self.quantity < 0) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ObjectItemInformationWithQuantity.quantity.")