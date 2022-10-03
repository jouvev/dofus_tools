import tmp.TypesFactory as pf
from tmp.types.GameContextBasicSpawnInformation import GameContextBasicSpawnInformation
from tmp.types.GameContextActorInformations import GameContextActorInformations
class GameFightFighterInformations(GameContextActorInformations):
   def __init__(self,input):
      self.previousPositions = []
      _val4 = 0
      super().__init__(input)
      self.spawnInfo = GameContextBasicSpawnInformation(input)
      self._waveFunc(input)
      _id3 = input.readUnsignedShort()
      self.stats = pf.TypesFactory.get_instance_id(_id3,input)
      _previousPositionsLen = input.readUnsignedShort()
      for _i4 in range(0,_previousPositionsLen):
         _val4 = input.readVarUhShort()
         if(_val4 < 0 or _val4 > 559) :
            raise RuntimeError("Forbidden value (" + _val4 + ") on elements of previousPositions.")
         self.previousPositions.append(_val4)
   
   def _waveFunc(self,input) :
      self.wave = input.readByte()
      if(self.wave < 0) :
         raise RuntimeError("Forbidden value (" + self.wave + ") on element of GameFightFighterInformations.wave.")