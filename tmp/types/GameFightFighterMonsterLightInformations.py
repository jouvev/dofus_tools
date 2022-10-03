from tmp.types.GameFightFighterLightInformations import GameFightFighterLightInformations
class GameFightFighterMonsterLightInformations(GameFightFighterLightInformations):
   def __init__(self,input):
      super().__init__(input)
      self._creatureGenericIdFunc(input)
   
   def _creatureGenericIdFunc(self,input) :
      self.creatureGenericId = input.readVarUhShort()
      if(self.creatureGenericId < 0) :
         raise RuntimeError("Forbidden value (" + self.creatureGenericId + ") on element of GameFightFighterMonsterLightInformations.creatureGenericId.")