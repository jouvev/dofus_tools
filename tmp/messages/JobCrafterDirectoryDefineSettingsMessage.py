from tmp.types.JobCrafterDirectorySettings import JobCrafterDirectorySettings
class JobCrafterDirectoryDefineSettingsMessage:
   def __init__(self,input):
      self.settings = JobCrafterDirectorySettings(input)