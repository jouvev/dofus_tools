from tmp.messages.PartyInvitationDetailsMessage import PartyInvitationDetailsMessage

class PartyInvitationDungeonDetailsMessage(PartyInvitationDetailsMessage):
   def __init__(self,input):
      self.playersDungeonReady = []
      _val2 = False
      super().__init__(input)
      self._dungeonIdFunc(input)
      _playersDungeonReadyLen = input.readUnsignedShort()
      for _i2 in range(0,_playersDungeonReadyLen):
         _val2 = input.readBoolean()
         self.playersDungeonReady.append(_val2)
   
   def _dungeonIdFunc(self,input) :
      self.dungeonId = input.readVarUhShort()
      if(self.dungeonId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.dungeonId) + ") on element of PartyInvitationDungeonDetailsMessage.dungeonId.")

   def resume(self):
      super().resume()
      print("dungeonId :",self.dungeonId)
      print("playersDungeonReady :",self.playersDungeonReady)
