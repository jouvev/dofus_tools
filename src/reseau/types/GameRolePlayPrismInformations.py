import src.reseau.TypesFactory as pf
from src.reseau.types.GameRolePlayActorInformations import GameRolePlayActorInformations

class GameRolePlayPrismInformations(GameRolePlayActorInformations):
   def __init__(self,input):
      super().__init__(input)
      _id1 = input.readUnsignedShort()
      self.prism = pf.TypesFactory.get_instance_id(_id1,input)

   def resume(self):
      super().resume()
