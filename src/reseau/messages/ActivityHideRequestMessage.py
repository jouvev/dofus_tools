class ActivityHideRequestMessage:
   def __init__(self,input):
      self._activityIdFunc(input)
   
   def _activityIdFunc(self,input) :
      self.activityId = input.readVarUhShort()
      if(self.activityId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.activityId) + ") on element of ActivityHideRequestMessage.activityId.")

   def resume(self):
      print("activityId :",self.activityId)
