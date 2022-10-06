from src.reseau.types.GameRolePlayActorInformations import GameRolePlayActorInformations

class GameRolePlayTreasureHintInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      self._npcIdFunc(input)
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readVarUhShort()
      if(self.npcId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of GameRolePlayTreasureHintInformations.npcId.")

   def resume(self):
      super().resume()
      print("npcId :",self.npcId)
