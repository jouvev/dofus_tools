class ExchangeCraftPaymentModificationRequestMessage:
   def __init__(self,input):
      self._quantityFunc(input)
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhLong()
      if(self.quantity < 0 or self.quantity > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.quantity + ") on element of ExchangeCraftPaymentModificationRequestMessage.quantity.")