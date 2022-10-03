from tmp.types.GuildInformations import GuildInformations
from tmp.types.HouseInstanceInformations import HouseInstanceInformations
class HouseGuildedInformations(HouseInstanceInformations):
   def __init__(self,input):
      super().__init__(input)
      self.guildInfo = GuildInformations(input)