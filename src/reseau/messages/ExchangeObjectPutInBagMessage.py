from src.reseau.messages.ExchangeObjectMessage import ExchangeObjectMessage
from src.reseau.types.ObjectItem import ObjectItem

class ExchangeObjectPutInBagMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self.object = ObjectItem(input)

   def resume(self):
      super().resume()
      self.object.resum()
