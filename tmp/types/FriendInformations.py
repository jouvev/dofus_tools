from tmp.types.AbstractContactInformations import AbstractContactInformations

class FriendInformations(AbstractContactInformations):
   def __init__(self,input):
      super().__init__(input)
      self._playerStateFunc(input)
      self._lastConnectionFunc(input)
      self._achievementPointsFunc(input)
      self._leagueIdFunc(input)
      self._ladderPositionFunc(input)
   
   def _playerStateFunc(self,input) :
      self.playerState = input.readByte()
      if(self.playerState < 0) :
         raise RuntimeError("Forbidden value (" + str(self.playerState) + ") on element of FriendInformations.playerState.")
   
   def _lastConnectionFunc(self,input) :
      self.lastConnection = input.readVarUhShort()
      if(self.lastConnection < 0) :
         raise RuntimeError("Forbidden value (" + str(self.lastConnection) + ") on element of FriendInformations.lastConnection.")
   
   def _achievementPointsFunc(self,input) :
      self.achievementPoints = input.readInt()
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarShort()
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()

   def resume(self):
      super().resume()
      print("playerState :",self.playerState)
      print("lastConnection :",self.lastConnection)
      print("achievementPoints :",self.achievementPoints)
      print("leagueId :",self.leagueId)
      print("ladderPosition :",self.ladderPosition)
