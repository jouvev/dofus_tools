from src.reseau.messages.PartyInvitationRequestMessage import PartyInvitationRequestMessage

class PartyInvitationDungeonRequestMessage(PartyInvitationRequestMessage):
   def __init__(self,input):
      super().__init__(input)
      self._dungeonIdFunc(input)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of PartyInvitationDungeonRequestMessage.dungeonId.")

   def resume(self):
      super().resume()
      print("dungeonId :",self.dungeonId)
