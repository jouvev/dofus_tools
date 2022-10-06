from src.reseau.types.BaseSpawnMonsterInformation import BaseSpawnMonsterInformation

class SpawnScaledMonsterInformation(BaseSpawnMonsterInformation):
   def __init__(self,input):
      super().__init__(input)
      self._creatureLevelFunc(input)
   
   def _creatureLevelFunc(self,input) :
      self.creatureLevel = input.readShort()
      if(self.creatureLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.creatureLevel) + ") on element of SpawnScaledMonsterInformation.creatureLevel.")

   def resume(self):
      super().resume()
      print("creatureLevel :",self.creatureLevel)
