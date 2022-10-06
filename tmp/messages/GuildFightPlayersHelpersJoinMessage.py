from tmp.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations

class GuildFightPlayersHelpersJoinMessage:
   def __init__(self,input):
      self._fightIdFunc(input)
      self.playerInfo = CharacterMinimalPlusLookInformations(input)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readDouble()
      if(self.fightId < 0 or self.fightId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GuildFightPlayersHelpersJoinMessage.fightId.")

   def resume(self):
      print("fightId :",self.fightId)
      self.playerInfo.resum()
