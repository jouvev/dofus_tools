import tmp.TypesFactory as pf
from tmp.types.GameRolePlayGroupMonsterInformations import GameRolePlayGroupMonsterInformations
class GameRolePlayGroupMonsterWaveInformations(GameRolePlayGroupMonsterInformations):
   def __init__(self,input):
      self.alternatives = []
      _id2 = 0
      _item2 = None
      super().__init__(input)
      self._nbWavesFunc(input)
      _alternativesLen = input.readUnsignedShort()
      for _i2 in range(0,_alternativesLen):
         _id2 = input.readUnsignedShort()
         _item2 = pf.TypesFactory.get_instance_id(_id2,input)
         self.alternatives.append(_item2)
   
   def _nbWavesFunc(self,input) :
      self.nbWaves = input.readByte()
      if(self.nbWaves < 0) :
         raise RuntimeError("Forbidden value (" + self.nbWaves + ") on element of GameRolePlayGroupMonsterWaveInformations.nbWaves.")