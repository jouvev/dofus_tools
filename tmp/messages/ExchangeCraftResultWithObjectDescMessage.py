from tmp.messages.ExchangeCraftResultMessage import ExchangeCraftResultMessage
from tmp.types.ObjectItemNotInContainer import ObjectItemNotInContainer

class ExchangeCraftResultWithObjectDescMessage(ExchangeCraftResultMessage):
   def __init__(self,input):
      super().__init__(input)
      self.objectInfo = ObjectItemNotInContainer(input)

   def resume(self):
      super().resume()
      self.objectInfo.resum()
