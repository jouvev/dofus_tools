class GroupTeleportPlayerAnswerMessage:
   def __init__(self,input):
      self._acceptFunc(input)
      self._requesterIdFunc(input)
   
   def _acceptFunc(self,input) :
      self.accept = input.readBoolean()
   
   def _requesterIdFunc(self,input) :
      self.requesterId = input.readVarUhLong()
      if(self.requesterId < 0 or self.requesterId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.requesterId + ") on element of GroupTeleportPlayerAnswerMessage.requesterId.")