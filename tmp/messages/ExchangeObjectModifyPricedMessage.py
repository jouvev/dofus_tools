from tmp.messages.ExchangeObjectMovePricedMessage import ExchangeObjectMovePricedMessage

class ExchangeObjectModifyPricedMessage(ExchangeObjectMovePricedMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
