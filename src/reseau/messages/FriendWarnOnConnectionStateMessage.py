class FriendWarnOnConnectionStateMessage:
   def __init__(self,input):
      self._enableFunc(input)
   
   def _enableFunc(self,input) :
      self.enable = input.readBoolean()

   def resume(self):
      print("enable :",self.enable)
