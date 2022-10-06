import tmp.TypesFactory as pf
from tmp.types.GameRolePlayNamedActorInformations import GameRolePlayNamedActorInformations

class GameRolePlayHumanoidInformations(GameRolePlayNamedActorInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.humanoidInfo = pf.TypesFactory.get_instance_id(_id1,input)
      self._accountIdFunc(input)
   
   def _accountIdFunc(self,input) :
      self.accountId = input.readInt()
      if(self.accountId < 0) :
         raise RuntimeError("Forbidden value (" + str(self.accountId) + ") on element of GameRolePlayHumanoidInformations.accountId.")

   def resume(self):
      super().resume()
      print("accountId :",self.accountId)
