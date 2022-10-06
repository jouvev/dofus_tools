class JobCrafterDirectoryEntryJobInfo:
   def __init__(self,input):
      self._jobIdFunc(input)
      self._jobLevelFunc(input)
      self._freeFunc(input)
      self._minLevelFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobCrafterDirectoryEntryJobInfo.jobId.")
   
   def _jobLevelFunc(self,input) :
      self.jobLevel = input.readUnsignedByte()
      if(self.jobLevel < 1 or self.jobLevel > 200) :
         raise RuntimeError("Forbidden value (" + str(self.jobLevel) + ") on element of JobCrafterDirectoryEntryJobInfo.jobLevel.")
   
   def _freeFunc(self,input) :
      self.free = input.readBoolean()
   
   def _minLevelFunc(self,input) :
      self.minLevel = input.readUnsignedByte()
      if(self.minLevel < 0 or self.minLevel > 255) :
         raise RuntimeError("Forbidden value (" + str(self.minLevel) + ") on element of JobCrafterDirectoryEntryJobInfo.minLevel.")

   def resume(self):
      print("jobId :",self.jobId)
      print("jobLevel :",self.jobLevel)
      print("free :",self.free)
      print("minLevel :",self.minLevel)
