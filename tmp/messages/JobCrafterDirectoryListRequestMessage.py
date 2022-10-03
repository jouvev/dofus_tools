class JobCrafterDirectoryListRequestMessage:
   def __init__(self,input):
      self._jobIdFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + self.jobId + ") on element of JobCrafterDirectoryListRequestMessage.jobId.")