from src.reseau.types.MountClientData import MountClientData

class ExchangeStartOkMountWithOutPaddockMessage:
   def __init__(self,input):
      self.stabledMountsDescription = []
      _item1 = None
      _stabledMountsDescriptionLen = input.readUnsignedShort()
      for _i1 in range(0,_stabledMountsDescriptionLen):
         _item1 = MountClientData(input)
         self.stabledMountsDescription.append(_item1)

   def resume(self):
      for e in self.stabledMountsDescription:
         e.resume()
