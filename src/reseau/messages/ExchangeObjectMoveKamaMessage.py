class ExchangeObjectMoveKamaMessage:
   def __init__(self,input):
      self._quantityFunc(input)
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarLong()
      if(self.quantity < -9007199254740992 or self.quantity > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ExchangeObjectMoveKamaMessage.quantity.")

   def resume(self):
      print("quantity :",self.quantity)
