from tmp.messages.AbstractPartyEventMessage import AbstractPartyEventMessage
class PartyMemberRemoveMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self._leavingPlayerIdFunc(input)
   
   def _leavingPlayerIdFunc(self,input) :
      self.leavingPlayerId = input.readVarUhLong()
      if(self.leavingPlayerId < 0 or self.leavingPlayerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.leavingPlayerId + ") on element of PartyMemberRemoveMessage.leavingPlayerId.")