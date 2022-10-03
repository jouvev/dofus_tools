from tmp.messages.PartyInvitationMessage import PartyInvitationMessage
class PartyInvitationDungeonMessage(PartyInvitationMessage):
   def __init__(self,input):
      super().__init__(input)
      self._dungeonIdFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + self.dungeonId + ") on element of PartyInvitationDungeonMessage.dungeonId.")