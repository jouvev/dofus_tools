from tmp.types.AccountTagInformation import AccountTagInformation

class FriendDeleteResultMessage:
   def __init__(self,input):
      self._successFunc(input)
      self.tag = AccountTagInformation(input)
   
   def _successFunc(self,input) :
      self.success = input.readBoolean()

   def resume(self):
      print("success :",self.success)
      self.tag.resum()
