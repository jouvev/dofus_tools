from src.reseau.messages.ExchangeCraftResultMessage import ExchangeCraftResultMessage
from src.reseau.types.ObjectItemNotInContainer import ObjectItemNotInContainer

class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
   def __init__(self,input):
      super().__init__(input)
      self.objectInfo = ObjectItemNotInContainer(input)

   def resume(self):
      super().resume()
      self.objectInfo.resume()
