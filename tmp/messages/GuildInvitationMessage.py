class GuildInvitationMessage:
   def __init__(self,input):
      self._targetIdFunc(input)
   
   def _targetIdFunc(self,input) :
      self.targetId = input.readVarUhLong()
      if(self.targetId < 0 or self.targetId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.targetId + ") on element of GuildInvitationMessage.targetId.")