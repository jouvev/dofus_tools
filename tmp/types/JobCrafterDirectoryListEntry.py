from tmp.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from tmp.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo

class JobCrafterDirectoryListEntry:
   def __init__(self,input):
      self.playerInfo = JobCrafterDirectoryEntryPlayerInfo(input)
      self.jobInfo = JobCrafterDirectoryEntryJobInfo(input)

   def resume(self):
      self.playerInfo.resum()
      self.jobInfo.resum()
