from src.reseau.types.JobCrafterDirectoryEntryPlayerInfo import JobCrafterDirectoryEntryPlayerInfo
from src.reseau.types.JobCrafterDirectoryEntryJobInfo import JobCrafterDirectoryEntryJobInfo
from src.reseau.types.EntityLook import EntityLook

class JobCrafterDirectoryEntryMessage:
   def __init__(self,input):
      self.jobInfoList = []
      _item2 = None
      self.playerInfo = JobCrafterDirectoryEntryPlayerInfo(input)
      _jobInfoListLen = input.readUnsignedShort()
      for _i2 in range(0,_jobInfoListLen):
         _item2 = JobCrafterDirectoryEntryJobInfo(input)
         self.jobInfoList.append(_item2)
      self.playerLook = EntityLook(input)

   def resume(self):
      self.playerInfo.resum()
      self.playerLook.resum()
      for e in self.jobInfoList:
         e.resume()
