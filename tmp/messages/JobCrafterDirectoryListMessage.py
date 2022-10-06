from tmp.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry

class JobCrafterDirectoryListMessage:
   def __init__(self,input):
      self.listEntries = []
      _item1 = None
      _listEntriesLen = input.readUnsignedShort()
      for _i1 in range(0,_listEntriesLen):
         _item1 = JobCrafterDirectoryListEntry(input)
         self.listEntries.append(_item1)

   def resume(self):
      for e in self.listEntries:
         e.resume()
