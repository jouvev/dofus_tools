from tmp.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
class JobCrafterDirectorySettingsMessage:
   def __init__(self,input):
      self.craftersSettings = []
      _item1 = None
      _craftersSettingsLen = input.readUnsignedShort()
      for _i1 in range(0,_craftersSettingsLen):
         _item1 = JobCrafterDirectorySettings(input)
         self.craftersSettings.append(_item1)