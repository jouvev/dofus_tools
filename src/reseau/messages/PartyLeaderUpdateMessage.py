from src.reseau.messages.AbstractPartyEventMessage import AbstractPartyEventMessage

class PartyLeaderUpdateMessage(AbstractPartyEventMessage):
   def __init__(self,input):
      super().__init__(input)
      self._partyLeaderIdFunc(input)
   
   def _partyLeaderIdFunc(self,input) :
      self.partyLeaderId = input.readVarUhLong()
      if(self.partyLeaderId < 0 or self.partyLeaderId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.partyLeaderId) + ") on element of PartyLeaderUpdateMessage.partyLeaderId.")

   def resume(self):
      super().resume()
      print("partyLeaderId :",self.partyLeaderId)
