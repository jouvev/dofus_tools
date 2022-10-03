class JobExperience:
   def __init__(self,input):
      self._jobIdFunc(input)
      self._jobLevelFunc(input)
      self._jobXPFunc(input)
      self._jobXpLevelFloorFunc(input)
      self._jobXpNextLevelFloorFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + self.jobId + ") on element of JobExperience.jobId.")
   
   def _jobLevelFunc(self,input) :
      self.jobLevel = input.readUnsignedByte()
      if(self.jobLevel < 0 or self.jobLevel > 255) :
         raise RuntimeError("Forbidden value (" + self.jobLevel + ") on element of JobExperience.jobLevel.")
   
   def _jobXPFunc(self,input) :
      self.jobXP = input.readVarUhLong()
      if(self.jobXP < 0 or self.jobXP > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.jobXP + ") on element of JobExperience.jobXP.")
   
   def _jobXpLevelFloorFunc(self,input) :
      self.jobXpLevelFloor = input.readVarUhLong()
      if(self.jobXpLevelFloor < 0 or self.jobXpLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.jobXpLevelFloor + ") on element of JobExperience.jobXpLevelFloor.")
   
   def _jobXpNextLevelFloorFunc(self,input) :
      self.jobXpNextLevelFloor = input.readVarUhLong()
      if(self.jobXpNextLevelFloor < 0 or self.jobXpNextLevelFloor > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.jobXpNextLevelFloor + ") on element of JobExperience.jobXpNextLevelFloor.")