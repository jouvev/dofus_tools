from tmp.types.AbstractContactInformations import AbstractContactInformations
class LeagueFriendInformations(AbstractContactInformations):
   def __init__(self,input):
      super().__init__(input)
      self._playerIdFunc(input)
      self._playerNameFunc(input)
      self._breedFunc(input)
      self._sexFunc(input)
      self._levelFunc(input)
      self._leagueIdFunc(input)
      self._totalLeaguePointsFunc(input)
      self._ladderPositionFunc(input)
   
   def _playerIdFunc(self,input) :
      self.playerId = input.readVarUhLong()
      if(self.playerId < 0 or self.playerId > 9007199254740992) :
         raise RuntimeError("Forbidden value (" + self.playerId + ") on element of LeagueFriendInformations.playerId.")
   
   def _playerNameFunc(self,input) :
      self.playerName = input.readUTF()
   
   def _breedFunc(self,input) :
      self.breed = input.readByte()
      if(self.breed < 0 or self.breed > 18) :
         raise RuntimeError("Forbidden value (" + self.breed + ") on element of LeagueFriendInformations.breed.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _levelFunc(self,input) :
      self.level = input.readVarUhShort()
      if(self.level < 0) :
         raise RuntimeError("Forbidden value (" + self.level + ") on element of LeagueFriendInformations.level.")
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarShort()
   
   def _totalLeaguePointsFunc(self,input) :
      self.totalLeaguePoints = input.readVarShort()
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()