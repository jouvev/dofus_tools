from tmp.messages.CompassUpdateMessage import CompassUpdateMessage
class CompassUpdatePartyMemberMessage(CompassUpdateMessage):
   def __init__(self,input):
      super().__init__(input)
      self._memberIdFunc(input)
      self._activeFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.memberId + ") on element of CompassUpdatePartyMemberMessage.memberId.")
   
   def _activeFunc(self,input) :
      self.active = input.readBoolean()