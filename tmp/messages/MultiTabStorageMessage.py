from tmp.types.StorageTabInformation import StorageTabInformation

class MultiTabStorageMessage:
   def __init__(self,input):
      self.tabs = []
      _item1 = None
      _tabsLen = input.readUnsignedShort()
      for _i1 in range(0,_tabsLen):
         _item1 = StorageTabInformation(input)
         self.tabs.append(_item1)

   def resume(self):
      for e in self.tabs:
         e.resume()
