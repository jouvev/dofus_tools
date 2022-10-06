from src.reseau.messages.ExchangeBidHouseInListAddedMessage import ExchangeBidHouseInListAddedMessage

class ExchangeBidHouseInListUpdatedMessage(ExchangeBidHouseInListAddedMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
