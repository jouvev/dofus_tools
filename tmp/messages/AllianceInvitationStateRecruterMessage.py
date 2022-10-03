class AllianceInvitationStateRecruterMessage:
   def __init__(self,input):
      self._recrutedNameFunc(input)
      self._invitationStateFunc(input)
   
   def _recrutedNameFunc(self,input) :
      self.recrutedName = input.readUTF()
   
   def _invitationStateFunc(self,input) :
      self.invitationState = input.readByte()
      if(self.invitationState < 0) :
         raise RuntimeError("Forbidden value (" + self.invitationState + ") on element of AllianceInvitationStateRecruterMessage.invitationState.")