class SocialNoticeMessage:
   def __init__(self,input):
      self._contentFunc(input)
      self._timestampFunc(input)
      self._memberIdFunc(input)
      self._memberNameFunc(input)
   
   def _contentFunc(self,input) :
      self.content = input.readUTF()
   
   def _timestampFunc(self,input) :
      self.timestamp = input.readInt()
      if(self.timestamp < 0) :
         raise RuntimeError("Forbidden value (" + self.timestamp + ") on element of SocialNoticeMessage.timestamp.")
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.memberId + ") on element of SocialNoticeMessage.memberId.")
   
   def _memberNameFunc(self,input) :
      self.memberName = input.readUTF()