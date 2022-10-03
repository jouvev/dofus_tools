class ActivityLockRequestMessage:
   def __init__(self,input):
      self._activityIdFunc(input)
      self._lockFunc(input)
   
   def _activityIdFunc(self,input) :
      self.activityId = input.readVarUhShort()
      if(self.activityId < 0) :
         raise RuntimeError("Forbidden value (" + self.activityId + ") on element of ActivityLockRequestMessage.activityId.")
   
   def _lockFunc(self,input) :
      self.lock = input.readBoolean()