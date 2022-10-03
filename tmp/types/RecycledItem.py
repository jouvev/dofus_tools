class RecycledItem:
   def __init__(self,input):
      self._idFunc(input)
      self._qtyFunc(input)
   
   def _idFunc(self,input) :
      self.id = input.readVarUhInt()
      if(self.id < 0) :
         raise RuntimeError("Forbidden value (" + self.id + ") on element of RecycledItem.id.")
   
   def _qtyFunc(self,input) :
      self.qty = input.readUnsignedInt()
      if(self.qty < 0 or self.qty > 4294967295) :
         raise RuntimeError("Forbidden value (" + self.qty + ") on element of RecycledItem.qty.")