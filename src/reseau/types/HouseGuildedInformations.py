from src.reseau.types.GuildInformations import GuildInformations
from src.reseau.types.HouseInstanceInformations import HouseInstanceInformations

class HouseGuildedInformations(HouseInstanceInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guildInfo = GuildInformations(input)

   def resume(self):
      super().resume()
      self.guildInfo.resume()
