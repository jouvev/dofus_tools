from tmp.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations

class GameRolePlayMountInformations(GameRolePlayNamedActorInformations):
   def __init__(self,input):
      super().__init__(input)
      self._ownerNameFunc(input)
      self._levelFunc(input)
   
   def _ownerNameFunc(self,input) :
      self.ownerName = input.readUTF()
   
   def _levelFunc(self,input) :
      self.level = input.readUnsignedByte()
      if(self.level < 0 or self.level > 255) :
         raise RuntimeError("Forbidden value (" + str(self.level) + ") on element of GameRolePlayMountInformations.level.")

   def resume(self):
      super().resume()
      print("ownerName :",self.ownerName)
      print("level :",self.level)
