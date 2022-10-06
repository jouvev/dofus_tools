from tmp.messages.PartyFollowMemberRequestMessage import PartyFollowMemberRequestMessage

class PartyFollowThisMemberRequestMessage(PartyFollowMemberRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._enabledFunc(input)
   
   def _enabledFunc(self,input) :
      self.enabled = input.readBoolean()

   def resume(self):
      super().resume()
      print("enabled :",self.enabled)
