class FriendStatusShareStateMessage:
   def __init__(self,input):
      self._shareFunc(input)
   
   def _shareFunc(self,input) :
      self.share = input.readBoolean()

   def resume(self):
      print("share :",self.share)
