class GuildKickRequestMessage:
   def __init__(self,input):
      self._kickedIdFunc(input)
   
   def _kickedIdFunc(self,input) :
      self.kickedId = input.readVarUhLong()
      if(self.kickedId < 0 or self.kickedId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.kickedId + ") on element of GuildKickRequestMessage.kickedId.")