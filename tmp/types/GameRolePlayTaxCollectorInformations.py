import tmp.TypesFactory as pf
from tmp.types.GameRolePlayActorInformations import GameRolePlayActorInformations
class GameRolePlayTaxCollectorInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.identification = pf.TypesFactory.get_instance_id(_id1,input)
      self._guildLevelFunc(input)
      self._taxCollectorAttackFunc(input)
   
   def _guildLevelFunc(self,input) :
      self.guildLevel = input.readUnsignedByte()
      if(self.guildLevel < 0 or self.guildLevel > 255) :
         raise RuntimeError("Forbidden value (" + self.guildLevel + ") on element of GameRolePlayTaxCollectorInformations.guildLevel.")
   
   def _taxCollectorAttackFunc(self,input) :
      self.taxCollectorAttack = input.readInt()