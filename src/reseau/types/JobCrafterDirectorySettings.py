class JobCrafterDirectorySettings:
   def __init__(self,input):
      self._jobIdFunc(input)
      self._minLevelFunc(input)
      self._freeFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobCrafterDirectorySettings.jobId.")
   
   def _minLevelFunc(self,input) :
      self.minLevel = input.readUnsignedByte()
      if(self.minLevel < 0 or self.minLevel > 255) :
         raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of JobCrafterDirectorySettings.minLevel.")
   
   def _freeFunc(self,input) :
      self.free = input.readBoolean()

   def resume(self):
      print("jobId :",self.jobId)
      print("minLevel :",self.minLevel)
      print("free :",self.free)
