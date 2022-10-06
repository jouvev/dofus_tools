class GuildMemberLeavingMessage:
   def __init__(self,input):
      self._kickedFunc(input)
      self._memberIdFunc(input)
   
   def _kickedFunc(self,input) :
      self.kicked = input.readBoolean()
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element of GuildMemberLeavingMessage.memberId.")

   def resume(self):
      print("kicked :",self.kicked)
      print("memberId :",self.memberId)
