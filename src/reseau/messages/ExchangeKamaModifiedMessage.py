from src.reseau.messages.ExchangeObjectMessage import ExchangeObjectMessage

class ExchangeKamaModifiedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self._quantityFunc(input)
   
   def _quantityFunc(self,input) :
      self.quantity = input.readVarUhLong()
      if(self.quantity < 0 or self.quantity > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.quantity) + ") on element of ExchangeKamaModifiedMessage.quantity.")

   def resume(self):
      super().resume()
      print("quantity :",self.quantity)
