from src.reseau.messages.ExchangeObjectMoveMessage import ExchangeObjectMoveMessage

class ExchangeObjectMovePricedMessage(ExchangeObjectMoveMessage):
   def __init__(self,input):
      super().__init__(input)
      self._priceFunc(input)
   
   def _priceFunc(self,input) :
      self.price = input.readVarUhLong()
      if(self.price < 0 or self.price > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.price) + ") on element of ExchangeObjectMovePricedMessage.price.")

   def resume(self):
      super().resume()
      print("price :",self.price)
