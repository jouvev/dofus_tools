from tmp.messages.ExchangeObjectMessage import ExchangeObjectMessage
from tmp.types.ObjectItem import ObjectItem
class ExchangeObjectAddedMessage(ExchangeObjectMessage):
   def __init__(self,input):
      super().__init__(input)
      self.object = ObjectItem(input)