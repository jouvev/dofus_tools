from tmp.types.PlayerStatus import PlayerStatus
from tmp.types.GameFightFighterInformations import GameFightFighterInformations
class GameFightFighterNamedInformations(GameFightFighterInformations):
   def __init__(self,input):
      super().__init__(input)
      self._nameFunc(input)
      self.status = PlayerStatus(input)
      self._leagueIdFunc(input)
      self._ladderPositionFunc(input)
      self._hiddenInPrefightFunc(input)
   
   def _nameFunc(self,input) :
      self.name = input.readUTF()
   
   def _leagueIdFunc(self,input) :
      self.leagueId = input.readVarShort()
   
   def _ladderPositionFunc(self,input) :
      self.ladderPosition = input.readInt()
   
   def _hiddenInPrefightFunc(self,input) :
      self.hiddenInPrefight = input.readBoolean()