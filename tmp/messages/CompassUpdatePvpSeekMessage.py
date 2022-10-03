from tmp.messages.CompassUpdateMessage import CompassUpdateMessage
class CompassUpdatePvpSeekMessage(CompassUpdateMessage):
   def __init__(self,input):
      super().__init__(input)
      self._memberIdFunc(input)
      self._memberNameFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.memberId + ") on element of CompassUpdatePvpSeekMessage.memberId.")
   
   def _memberNameFunc(self,input) :
      self.memberName = input.readUTF()