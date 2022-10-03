class ActivityHideRequestMessage:
   def __init__(self,input):
      self._activityIdFunc(input)
   
   def _activityIdFunc(self,input) :
      self.activityId = input.readVarUhShort()
      if(self.activityId < 0) :
         raise RuntimeError("Forbidden value (" + self.activityId + ") on element of ActivityHideRequestMessage.activityId.")