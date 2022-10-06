from tmp.types.CharacterMinimalPlusLookInformations import CharacterMinimalPlusLookInformations

class GuildFightPlayersEnemiesListMessage:
   def __init__(self,input):
      self.playerInfo = []
      _item2 = None
      self._fightIdFunc(input)
      _playerInfoLen = input.readUnsignedShort()
      for _i2 in range(0,_playerInfoLen):
         _item2 = CharacterMinimalPlusLookInformations(input)
         self.playerInfo.append(_item2)
   
   def _fightIdFunc(self,input) :
      self.fightId = input.readDouble()
      if(self.fightId < 0 or self.fightId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + str(self.fightId) + ") on element of GuildFightPlayersEnemiesListMessage.fightId.")

   def resume(self):
      print("fightId :",self.fightId)
      for e in self.playerInfo:
         e.resume()
