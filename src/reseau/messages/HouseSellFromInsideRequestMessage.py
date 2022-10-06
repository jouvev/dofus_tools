from src.reseau.messages.HouseSellRequestMessage import HouseSellRequestMessage

class HouseSellFromInsideRequestMessage(HouseSellRequestMessage):
   def __init__(self,input):
      super().__init__(input)

   def resume(self):
      super().resume()
