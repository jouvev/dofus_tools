from src.reseau.types.GameFightFighterNamedInformations import GameFightFighterNamedInformations

class GameFightMutantInformations(GameFightFighterNamedInformations):
   def __init__(self,input):
      super().__init__(input)
      self._powerLevelFunc(input)
   
   def _powerLevelFunc(self,input) :
      self.powerLevel = input.readByte()
      if(self.powerLevel < 0) :
         raise RuntimeError("Forbidden value (" + str(self.powerLevel) + ") on element of GameFightMutantInformations.powerLevel.")

   def resume(self):
      super().resume()
      print("powerLevel :",self.powerLevel)
