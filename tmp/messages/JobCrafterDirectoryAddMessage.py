from tmp.types.JobCrafterDirectoryListEntry import JobCrafterDirectoryListEntry

class JobCrafterDirectoryAddMessage:
   def __init__(self,input):
      self.listEntry = JobCrafterDirectoryListEntry(input)

   def resume(self):
      self.listEntry.resum()
