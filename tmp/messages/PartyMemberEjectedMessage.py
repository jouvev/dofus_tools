from tmp.messages.PartyMemberRemoveMessage import PartyMemberRemoveMessage
class PartyMemberEjectedMessage(PartyMemberRemoveMessage):
   def __init__(self,input):
      super().__init__(input)
      self._kickerIdFunc(input)
   
   def _kickerIdFunc(self,input) :
      self.kickerId = input.readVarUhLong()
      if(self.kickerId < 0 or self.kickerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.kickerId + ") on element of PartyMemberEjectedMessage.kickerId.")