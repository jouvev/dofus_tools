class JobBookSubscription:
   def __init__(self,input):
      self._jobIdFunc(input)
      self._subscribedFunc(input)
   
   def _jobIdFunc(self,input) :
      self.jobId = input.readByte()
      if(self.jobId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.jobId) + ") on element of JobBookSubscription.jobId.")
   
   def _subscribedFunc(self,input) :
      self.subscribed = input.readBoolean()

   def resume(self):
      print("jobId :",self.jobId)
      print("subscribed :",self.subscribed)
