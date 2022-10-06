from tmp.messages.ExchangeStartOkMountWithOutPaddockMessage import ExchangeStartOkMountWithOutPaddockMessage
from tmp.types.MountClientData import MountClientData

class ExchangeStartOkMountMessage(ExchangeStartOkMountWithOutPaddockMessage):
   def __init__(self,input):
      self.paddockedMountsDescription = []
      _item1 = None
      super().__init__(input)
      _paddockedMountsDescriptionLen = input.readUnsignedShort()
      for _i1 in range(0,_paddockedMountsDescriptionLen):
         _item1 = MountClientData(input)
         self.paddockedMountsDescription.append(_item1)

   def resume(self):
      super().resume()
      for e in self.paddockedMountsDescription:
         e.resume()
