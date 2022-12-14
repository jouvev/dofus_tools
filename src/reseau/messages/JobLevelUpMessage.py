from src.reseau.types.JobDescription import JobDescription

class JobLevelUpMessage:
   def __init__(self,input):
      self._newLevelFunc(input)
      self.jobsDescription = JobDescription(input)
   
   def _newLevelFunc(self,input) :
      self.newLevel = input.readUnsignedByte()
      if(self.newLevel < 0 or self.newLevel > 255) :
         raise RuntimeError("Forbidden value (" + str(self.newLevel) + ") on element of JobLevelUpMessage.newLevel.")

   def resume(self):
      print("newLevel :",self.newLevel)
      self.jobsDescription.resume()
