from src.reseau.types.GameRolePlayHumanoidInformations import GameRolePlayHumanoidInformations

class GameRolePlayMutantInformations(GameRolePlayHumanoidInformations):
   def __init__(self,input):
      super().__init__(input)
      self._monsterIdFunc(input)
      self._powerLevelFunc(input)
   
   def _monsterIdFunc(self,input) :
      self.monsterId = input.readVarUhShort()
      if(self.monsterId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.monsterId) + ") on element of GameRolePlayMutantInformations.monsterId.")
   
   def _powerLevelFunc(self,input) :
      self.powerLevel = input.readByte()

   def resume(self):
      super().resume()
      print("monsterId :",self.monsterId)
      print("powerLevel :",self.powerLevel)
