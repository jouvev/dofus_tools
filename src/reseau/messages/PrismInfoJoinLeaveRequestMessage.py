class PrismInfoJoinLeaveRequestMessage:
   def __init__(self,input):
      self._joinFunc(input)
   
   def _joinFunc(self,input) :
      self.join = input.readBoolean()

   def resume(self):
      print("join :",self.join)
