from src.reseau.messages.ExchangeMountsStableAddMessage import ExchangeMountsStableAddMessage

class ExchangeMountsStableBornAddMessage(ExchangeMountsStableAddMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
