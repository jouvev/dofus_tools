class GuildInvitationStateRecrutedMessage:
   def __init__(self,input):
      self._invitationStateFunc(input)
   
   def _invitationStateFunc(self,input) :
      self.invitationState = input.readByte()
      if(self.invitationState < 0) :
         raise RuntimeError("Forbidden value (" + self.invitationState + ") on element of GuildInvitationStateRecrutedMessage.invitationState.")