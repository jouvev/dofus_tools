class ExchangeObjectMoveMessage:
   def __init__(self,input):
      self._objectUIDFunc(input)
      self._quantityFunc(input)
   
   def _objectUIDFunc(self,input) :
      self.objectUID = input.readVarUhInt()
      if(self.objectUID < 0) :
         raise RuntimeError("Forbidden value (" + str(self.objectUID) + ") on element of ExchangeObjectMoveMessage.objectUID.")
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarInt()

   def resume(self):
      print("objectUID :",self.objectUID)
      print("quantity :",self.quantity)
