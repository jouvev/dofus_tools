class FriendDeleteRequestMessage:
   def __init__(self,input):
      self._accountIdFunc(input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of FriendDeleteRequestMessage.accountId.")

   def resume(self):
      print("accountId :",self.accountId)
