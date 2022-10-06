class GuildUpdateNoteMessage:
   def __init__(self,input):
      self._memberIdFunc(input)
      self._noteFunc(input)
   
   def _memberIdFunc(self,input) :
      self.memberId = input.readVarUhLong()
      if(self.memberId < 0 or self.memberId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.memberId) + ") on element of GuildUpdateNoteMessage.memberId.")
   
   def _noteFunc(self,input) :
      self.note = input.readUTF()

   def resume(self):
      print("memberId :",self.memberId)
      print("note :",self.note)
