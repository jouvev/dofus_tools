import tmp.TypesFactory as pf
from tmp.types.GameRolePlayActorInformations import GameRolePlayActorInformations
class GameRolePlayPrismInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.prism = pf.TypesFactory.get_instance_id(_id1,input)