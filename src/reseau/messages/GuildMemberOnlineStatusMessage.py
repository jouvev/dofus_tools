class GuildMemberOnlineStatusMessage:
   def __init__(self,input):
      self._memberIdFunc(input)
      self._onlineFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element of GuildMemberOnlineStatusMessage.memberId.")
   
   def _onlineFunc(self,input) :
      self.online = input.readBoolean()

   def resume(self):
      print("memberId :",self.memberId)
      print("online :",self.online)
