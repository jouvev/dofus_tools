class GuildKickRequestMessage:
   def __init__(self,input):
      self._kickedIdFunc(input)
   
   def _kickedIdFunc(self,input) :
      self.kickedId = input.readVarUhLong()
      if(self.kickedId < 0 or self.kickedId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.kickedId) + ") on element of GuildKickRequestMessage.kickedId.")

   def resume(self):
      print("kickedId :",self.kickedId)
