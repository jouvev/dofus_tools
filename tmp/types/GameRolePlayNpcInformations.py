from tmp.types.GameRolePlayActorInformations import GameRolePlayActorInformations

class GameRolePlayNpcInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      self._npcIdFunc(input)
      self._sexFunc(input)
      self._specialArtworkIdFunc(input)
   
   def _npcIdFunc(self,input) :
      self.npcId = input.readVarUhShort()
      if(self.npcId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.npcId) + ") on element of GameRolePlayNpcInformations.npcId.")
   
   def _sexFunc(self,input) :
      self.sex = input.readBoolean()
   
   def _specialArtworkIdFunc(self,input) :
      self.specialArtworkId = input.readVarUhShort()
      if(self.specialArtworkId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.specialArtworkId) + ") on element of GameRolePlayNpcInformations.specialArtworkId.")

   def resume(self):
      super().resume()
      print("npcId :",self.npcId)
      print("sex :",self.sex)
      print("specialArtworkId :",self.specialArtworkId)
