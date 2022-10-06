from tmp.types.MountClientData import MountClientData

class ExchangeMountsStableAddMessage:
   def __init__(self,input):
      self.mountDescription = []
      _item1 = None
      _mountDescriptionLen = input.readUnsignedShort()
      for _i1 in range(0,_mountDescriptionLen):
         _item1 = MountClientData(input)
         self.mountDescription.append(_item1)

   def resume(self):
      for e in self.mountDescription:
         e.resume()
