from tmp.types.JobDescription import JobDescription
class JobLevelUpMessage:
   def __init__(self,input):
      self._newLevelFunc(input)
      self.jobsDescription = JobDescription(input)
   
   def _newLevelFunc(self,input) :
      self.newLevel = input.readUnsignedByte()
      if(self.newLevel < 0 or self.newLevel > 255) :
         raise RuntimeError("Forbidden value (" + self.newLevel + ") on element of JobLevelUpMessage.newLevel.")