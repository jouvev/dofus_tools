class ObjectJobAddedMessage:
   def __init__(self,input):
      self._jobIdFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of ObjectJobAddedMessage.jobId.")

   def resume(self):
      print("jobId :",self.jobId)
