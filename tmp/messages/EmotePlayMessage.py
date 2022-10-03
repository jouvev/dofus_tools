from tmp.messages.EmotePlayAbstractMessage import EmotePlayAbstractMessage
class EmotePlayMessage(EmotePlayAbstractMessage):
   def __init__(self,input):
      super().__init__(input)
      self._actorIdFunc(input)
      self._accountIdFunc(input)
   
   def _actorIdFunc(self,input) :
      self.actorId = input.readDouble()
      if(self.actorId < -9007199254740992 or self.actorId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.actorId + ") on element of EmotePlayMessage.actorId.")
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + self.accountId + ") on element of EmotePlayMessage.accountId.")